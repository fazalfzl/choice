import qrcode
from PIL import Image, ImageDraw, ImageFont

from common_support.utils import get_product_details_by_name, Config




def add_newline_to_table_data(table_data):
    for i in range(len(table_data)):
        item = table_data[i][0]
        if len(item) > 13:
            new_item = ''
            for j in range(0, len(item), 13):
                new_item += item[j:j + 13] + '\n'
            table_data[i][0] = new_item.rstrip('\n')
    return table_data


def generate_bill(table_data=None):
    config = Config()
    bill_width = config.get("bill_width") or 400
    bill_width = int(bill_width)
    height = 600
    dpi = 1200
    qr_size = 200
    table_cell_height = 50
    cell_widths = [int(bill_width / 2.5), int(bill_width / 5.2), int(bill_width / 5.2), int(bill_width / 4)]
    table_header_font = ImageFont.truetype('arialbd.ttf', 18)  # Use a bold font for table headers
    table_content_font = ImageFont.truetype('arialbd.ttf', 16)  # Use a bold font for table content
    total_font = ImageFont.truetype('arialbd.ttf', 25)
    headers = ['Item', 'Price', 'Qty', 'Amount']

    height = (len(table_data)+1)*table_cell_height + 20000
    image = Image.new('RGB', (bill_width, height), 'white')
    draw = ImageDraw.Draw(image)
    # Draw table headers
    for i, header in enumerate(headers):
        header_position = (sum(cell_widths[:i]), 0)
        draw.rectangle([(header_position[0], header_position[1]),
                        (header_position[0] + cell_widths[i], header_position[1] + table_cell_height)],
                       fill='white')
        draw.text((header_position[0] + 10, header_position[1] + 10), header, fill='black', font=table_header_font)

    # Example table data

    total_amount = 0
    qr_text=""

    config = Config()
    code_length = int(config.get("code_length"))
    qty_length = int(config.get("qty_length"))
    first_char = config.get("first_char")

    for row in table_data:
        total_amount += float(row[3])

        product_details = get_product_details_by_name(row[0])
        code = product_details['code'].zfill(code_length)
        qty = str(row[2].replace('.', "")).zfill(qty_length)  # Ensure qty is 5 characters long with leading zeros
        qr_text += f"{first_char}{code}{qty}\n"

    print(qr_text)

    print("Total amount = ", total_amount)

    table_data = add_newline_to_table_data(table_data)
    # Draw table rows
    row_height = table_cell_height + 10
    for i, row in enumerate(table_data):
        row_position = (0, (i + 1) * row_height)
        for j, cell in enumerate(row):
            cell_position = (sum(cell_widths[:j]), row_position[1])
            draw.rectangle([(cell_position[0], cell_position[1]),
                            (cell_position[0] + cell_widths[j], cell_position[1] + table_cell_height)],
                           fill='white')
            draw.text((cell_position[0] + 10, cell_position[1] + 10), cell, fill='black', font=table_content_font)

    # Draw the total amount at the bottom in a larger font
    total_text = f"Total amount: ${total_amount}"
    total_position = (0, (len(table_data) + 1) * row_height)
    draw.text((total_position[0] + 10, total_position[1] + 10), total_text, fill='black', font=total_font)

    # Generate the QR code
    qr_data = qr_text
    qr = qrcode.QRCode(version=1, box_size=10, border=1)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Resize the QR code image
    qr_image = qr_image.resize((qr_size, qr_size))  # Adjust the size as needed

    # Paste the QR code at the bottom of the bill
    qr_position = (
    bill_width // 2 - qr_image.width // 2, (len(table_data) + 2) * row_height)  # Adjust the position as needed
    image.paste(qr_image, qr_position)

    # Save the bill as a PNG file
    image.save('bill.png', dpi=(dpi, dpi))
