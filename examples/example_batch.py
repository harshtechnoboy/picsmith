from image_processes.batch_process import batch_resize

batch_resize("/path/to/image", (1024, 768))
print("Batch resize completed!")

from image_processes.batch_process import batch_compress

batch_compress("/path/to/image", quality=70)
print("Batch compress completed!")