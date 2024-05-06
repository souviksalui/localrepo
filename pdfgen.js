<script type="text/javascript">
    async function downloadPdf() {

            const url = './print-templates/pquot-template.pdf';
            const existingPdfBytes = await fetch(url).then(res => res.arrayBuffer());

    // Getting the document
    const pdfDoc = await PDFLib.PDFDocument.load(existingPdfBytes);

    // Getting the first page
    const pages = pdfDoc.getPages();
    const firstPage = pages[0];

    // Customer name
    firstPage.drawText('Customer name is here with more text (GAR004) quick brown customerm jumps over lazy dog.', {
        x: 10.5*9,
    y: 76.6*9,
    size: 10,
    maxWidth: 28*9, // Wrap text with one line. WOW :O
    lineHeight: 1.5*9
            });

    // Currency short code
    firstPage.drawText('LKR', {
        x: 10.5*9,
    y: 73.5*9,
    size: 10
            });

    var itemName = 'Here is the item name with some really really long text and quick brown fox jumps over lazy dog. long text and quick brown fox jumps over lazy dog:)';
    // Item name
    firstPage.drawText(itemName, {
        x: 5*9,
    y: 67*9,
    size: 10,
    maxWidth: 31*9,
    lineHeight: 2*9
            });

    const pdfDataUri = await pdfDoc.saveAsBase64({dataUri: true });
    document.getElementById('pdf').src = pdfDataUri;
        }

</script>