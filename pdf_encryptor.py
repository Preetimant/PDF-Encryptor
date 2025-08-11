#!/usr/bin/env python3
"""
Encrypt a PDF file with AES-256, using separate user and owner passwords.
Requires pypdf>=3.14.0 with crypto extras installed.
Use: pip install pypdf[crypto] to install the dependency
Usage: python protector.py <input.pdf> <output.pdf> -u <"userpassword"> -o <"ownerpassword">
--user-pwd (or) -o "readerpass"  | for read-only (no other permissions)
--owner-pwd (or) -o "adminpass"  | for full permissions

Skip setting -o to make user==owner
"""

import argparse
import sys
from pypdf import PdfReader, PdfWriter

def aes256_protect(input_pdf_path: str, output_pdf_path: str, user_pwd: str, owner_pwd: str = None):
    if owner_pwd is None:
        owner_pwd = user_pwd

    # Read & Copy
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt under AES-256
    writer.encrypt(
        user_password = user_pwd,
        owner_password = owner_pwd,
        algorithm ="AES-256",
        permissions_flag = 0
    )

    # Ensure PDF version 2.0 header
    writer._header = b"%PDF-2.0"

    # Write out
    with open(output_pdf_path, "wb") as out_f:
        writer.write(out_f)


def parse_args():
    p = argparse.ArgumentParser(description = "Encrypt a PDF with AES-256 (user + owner passwords).", usage="%(prog)s <input.pdf> <output.pdf> -u <userpassword> [-o <ownerpassword>]")
    p.add_argument("input", help = "Path to source PDF")
    p.add_argument("output", help = "Path to write encrypted PDF")
    p.add_argument(
                    "-u", "--user-pwd", required = True,
                    help="User password (required to open the PDF)"
                )
    p.add_argument(
                    "-o", "--owner-pwd", default = None,
                    help="Owner password (if omitted, defaults to user password)"
                )
    return p.parse_args()


def main():
    args = parse_args()
    try:
        aes256_protect(
            input_pdf_path = args.input,
            output_pdf_path = args.output,
            user_pwd = args.user_pwd,
            owner_pwd = args.owner_pwd
        )
        print(f"Successfully saved encrypted PDF as: {args.output}")
    except FileNotFoundError:
        print(f"Input file not found: {args.input}", file = sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error encrypting PDF: {e}", file = sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()