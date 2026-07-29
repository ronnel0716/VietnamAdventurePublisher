"""
pdf_publisher.py

Exports a Handbook to PDF.

Current implementation:
- Uses the WordPublisher to generate a temporary DOCX.
- PDF conversion is intentionally left as a platform-specific step.
"""

from pathlib import Path
import tempfile

from .word_publisher import WordPublisher


class PDFPublisher:
    """
    Publish a Handbook as PDF.
    """

    def __init__(self):
        self.word_publisher = WordPublisher()

    def publish(self, handbook, output_path):
        """
        Publish a handbook to PDF.

        Parameters
        ----------
        handbook
            Handbook model.

        output_path : str | Path
            Destination PDF filename.

        Returns
        -------
        Path
            Output PDF path.

        Raises
        ------
        NotImplementedError
            Until a PDF backend is selected.
        """

        output_path = Path(output_path)

        with tempfile.TemporaryDirectory() as tmp:

            docx_path = Path(tmp) / "handbook.docx"

            self.word_publisher.publish(
                handbook,
                str(docx_path)
            )

            raise NotImplementedError(
                "DOCX generation is complete. "
                "Configure a PDF backend (LibreOffice, "
                "Microsoft Word COM, or another converter) "
                "to produce the final PDF."
            )

        return output_path