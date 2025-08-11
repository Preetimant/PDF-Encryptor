# PDF Encryptor (AES-256, Python)

This **Python-based PDF encryption tool** secures PDF files with **AES-256 encryption**, supporting separate user and owner passwords for tiered access control. It is compatible with the PDF 2.0 standard and is ideal for protecting sensitive documents.

---

## Features

- **AES-256 Encryption**  
  Uses modern 256-bit Advanced Encryption Standard to protect PDF contents.

- **Dual Password Support**  
  - **User Password**: Required to open the file (read-only by default).  
  - **Owner Password**: Grants full permissions such as printing and editing. If omitted, defaults to the user password.

- **Permission Restrictions**  
  Defaults to view-only mode (no printing, copying, or editing).  
  Permissions can be customized in the code if needed.

- **Simple Command-Line Interface**  
  Works directly from the terminal with clear usage options.

- **Error Handling**  
  Detects missing files and common input errors, providing user-friendly messages.

---

## Requirements

- **Python 3.x**  
- **pypdf** with crypto extras (version ≥ 3.14.0)  
  Install via:  
  ```bash
  pip install pypdf[crypto]
  ````

---

## Usage

```bash
python protector.py <input.pdf> <output.pdf> -u "userpassword" -o "ownerpassword"
```
**OR**
```bash
chmod +x pdf_encryptor.py
./pdf_encryptor.py <input.pdf> <output.pdf> -u "userpassword" -o "ownerpassword"
```
### Examples

**1. User password only (read-only):**

```bash
python protector.py input.pdf output.pdf -u "readerpass"
```

**2. Separate user and owner passwords:**

```bash
python protector.py input.pdf output.pdf -u "readerpass" -o "adminpass"
```

**Notes:**

* Skipping `-o` sets the owner password equal to the user password.
* Owner password provides full control; user password is view-only by default.

---

## Working

1. Reads the source PDF and copies all its pages into a new PDF container.
2. Applies AES-256 encryption with the provided user/owner passwords.
3. Sets permissions to allow viewing but disable printing, copying, and editing by default.
4. Writes the encrypted file to the specified output path, ensuring it meets PDF 2.0 compatibility.

---
