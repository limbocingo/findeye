import base64
import io

from django.core.files.uploadedfile import UploadedFile
from django.db.models import Model
from PIL import Image, UnidentifiedImageError


def get_image(encoded: str) -> tuple[bytes, str]:
    """Decodes a base64 string.

    .. versionadded:: 1.0

    Parameters
    -----------
    encoded: :class:`str`
        The encoded base64 image.
    
    Returns
    --------
    :class:`tuple[bytes, str]`
        The image in in bytes and the format of the image (for example: .png).
    """

    format, b64image = encoded.split(',')
    image = base64.b64decode(b64image)

    return (image, format)

def upload_image(object: Model, field: str, file: UploadedFile, resize: tuple[int, int] = None) -> tuple[bytes, str, str]:
    """Saves a base64 encoded image into a :class:`django.db.models.TextField`.

    .. versionadded:: 1.0

    Parameters
    -----------
    object: :class:`django.db.models.Model`
        Instance of the Model.
    field: :class:`str`
        In what field the BASE64 image will be stored.
        Have in mind that will be stored as a string.
    file: :class:`django.core.files.uploadedfile.UploadedFile`
        The file recieved from the response.
    resize: Optional[:class:`tuple[int, int]`]
        Height and width of the image.

    Returns
    --------
    :class:`tuple[bytes, str, str]`
        This will return the next: image, format (for example: .png) and error message.
        Exactly in this order.
    """

    if not file:
        return None, None, 'This field is required.'

    if file.size == 8*1024*1024:
        return None, None, 'Size too big. Max 8MB.'

    try:
        image = Image.open(file.open())
    except UnidentifiedImageError:
        return None, None, 'Bad format.'

    if resize:
        image.thumbnail(resize)

    with io.BytesIO() as output:
        image.save(output, format=image.format)
        content = output.getvalue()

    format = image.format.lower()

    b64encoded = f'{format},' + base64.b64encode(content).decode()

    setattr(object, field, b64encoded)
    object.save()

    return content, format, None
