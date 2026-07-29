"""
application.py

Main application entry point for the Vietnam Adventure Publisher.
"""

from vap.document.reader import DocumentReader
from vap.publisher.publisher import Publisher
from vap.publishing.word_publisher import WordPublisher
from vap.publishing.pdf_publisher import PDFPublisher


class Application:
    """
    Coordinates the complete publishing workflow.
    """

    def __init__(self):
        self.reader = DocumentReader()
        self.publisher = Publisher()
        self.word_publisher = WordPublisher()
        self.pdf_publisher = PDFPublisher()

    def build_handbook(self, source_path):
        """
        Read the source document and build the semantic handbook.
        """
        document = self.reader.read(source_path)
        return self.publisher.publish(document)

    def publish_word(self, source_path, output_path):
        """
        Generate a DOCX publication.
        """
        handbook = self.build_handbook(source_path)
        return self.word_publisher.publish(handbook, output_path)

    def publish_pdf(self, source_path, output_path):
        """
        Generate a PDF publication.
        """
        handbook = self.build_handbook(source_path)
        return self.pdf_publisher.publish(handbook, output_path)