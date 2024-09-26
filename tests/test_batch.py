from image_processes.batch_process import batch_resize

batch_resize("images", (600, 600))

from image_processes.batch_process import batch_compress

batch_compress("images", quality=60)