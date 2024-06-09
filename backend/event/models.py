from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Participant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        data = [self.name, self.surname, self.email]
        qr_image = qrcode.make(data)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        file_name = f"qr_code-{self.name}-{self.surname}-{self.email}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer), save=False)
        canvas.close()
        return super().save(*args, **kwargs)

