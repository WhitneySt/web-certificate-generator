import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from reportlab.pdfgen import canvas
import logging

class CertificateGenerator:
    def __init__(self, excel_path, template_path, output_folder, font_folder='fonts'):
        self.excel_path = excel_path
        self.template_path = template_path
        self.output_folder = output_folder
        self.font_folder = font_folder
        
        # Configure styles
        self.styles = {
            'name': {
                'font': 'RobotoMono-Bold.ttf',
                'size': 50,
                'color': '#280384',
                'position_y': 250,
                'spacing': -3
            },
            'id': {
                'font': 'RobotoMono-Bold.ttf',
                'size': 39,
                'color': '#280384',
                'position_y': 342,
                'position_x': 610,
                'spacing': -2
            }
        }
        
        self._setup_logging()
    
    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def _load_font(self, font_name, size):
        try:
            font_path = os.path.join(self.font_folder, font_name)
            return ImageFont.truetype(font_path, size)
        except Exception as e:
            logging.warning(f'Error loading font {font_name}: {e}')
            return ImageFont.load_default()
    
    def _draw_text_with_spacing(self, draw, text, style, image_width, centered=True):
        font = self._load_font(style['font'], style['size'])
        spacing = style.get('spacing', 0)
        
        # Calculate total width with spacing
        total_width = sum(
            draw.textlength(char, font=font) for char in text
        ) + spacing * (len(text) - 1)
        
        # Calculate starting position
        if centered:
            x = (image_width - total_width) // 2
        else:
            x = style.get('position_x', 0)
        
        # Draw each character
        for char in text:
            draw.text(
                (x, style['position_y']),
                char,
                font=font,
                fill=style['color']
            )
            x += draw.textlength(char, font=font) + spacing
    
    def generate_certificate(self, name, id_number):
        try:
            # Load template
            image = Image.open(self.template_path)
            draw = ImageDraw.Draw(image)
            
            # Generate filename
            date = datetime.now().strftime("%Y%m%d")
            filename = f"{date} {name.upper()}"
            
            # Draw text
            self._draw_text_with_spacing(draw, name, self.styles['name'], image.width)
            self._draw_text_with_spacing(
                draw, id_number, 
                self.styles['id'], 
                image.width, 
                centered=False
            )
            
            # Save files
            pdf_path = os.path.join(self.output_folder, f'{filename}.pdf')
            self._save_as_pdf(image, pdf_path)
            
            logging.info(f'Certificate generated: {filename}')
            return pdf_path
            
        except Exception as e:
            logging.error(f'Error generating certificate for {name}: {e}')
            raise
    
    def _save_as_pdf(self, image, pdf_path):
        c = canvas.Canvas(pdf_path, pagesize=image.size)
        temp_image_path = pdf_path + '.temp.png'
        
        try:
            image.save(temp_image_path)
            c.drawImage(temp_image_path, 0, 0, width=image.width, height=image.height)
            c.save()
        finally:
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)
    
    def generate_all(self):
        try:
            df = pd.read_excel(self.excel_path)
            total = len(df)
            generated = 0
            
            logging.info(f'Starting generation of {total} certificates')
            
            for _, row in df.iterrows():
                try:
                    self.generate_certificate(
                        name=row['nombre_completo'],
                        id_number=str(row['identificacion'])
                    )
                    generated += 1
                except Exception as e:
                    logging.error(f'Error with certificate: {e}')
            
            logging.info(f'Generated {generated} out of {total} certificates')
            
        except Exception as e:
            logging.error(f'Error in batch generation: {e}')
            raise