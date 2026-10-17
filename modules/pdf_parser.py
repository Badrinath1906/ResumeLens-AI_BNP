
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)

        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception as exc:
                raise ValueError(
                    "The PDF is password-protected."
                ) from exc

        extracted_pages = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_pages.append(page_text)

        extracted_text = "\n".join(extracted_pages).strip()

        if not extracted_text:
            raise ValueError(
                "No readable text found. The PDF may be scanned "
                "or contain no extractable text."
            )

        return extracted_text

    except ValueError:
        raise

    except Exception as exc:
        raise ValueError(
            "Unable to read this PDF. Please upload a valid PDF."
        ) from exc
