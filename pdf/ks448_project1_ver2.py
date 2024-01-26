import sys
import numpy as np
def pgmFileRead(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()     
        
        format_str = lines[0].strip()
        
        comments = []
        i = 1
        
        while i < len(lines) and lines[i].startswith("#"):
            comments.append(lines[i].strip())
            i += 1
        
        img_start_index = i
        
       
        img_header = lines[img_start_index:img_start_index + 3]
        width, height = map(int, img_header[0].split())
        max_value = int(img_header[1])

        
        pixel_data = [int(val) for line in lines[img_start_index + 2:] for val in line.split()]
        img = np.array(pixel_data).reshape(height, width)

    return (format_str, comments, width, height, max_value), img




def image_save(output_header, image_array, fileName):
    modified_header = list(output_header)
    format_str = modified_header[0]
    comments = modified_header[1]
    width, height = image_array.shape[1], image_array.shape[0]
    modified_header[2] = f"{width} {height}"
    del modified_header[3]

    with open(fileName, 'w') as f:
        f.write(format_str + '\n')
        
        for comment_line in comments:
            f.write(comment_line + '\n')

        for line in modified_header[2:]:
            f.write(str(line) + '\n')  
        
        for row in image_array:
            f.write(' '.join(map(str, row)) + '\n')


            
def ppmFileSave(output_header, image_array, file_name):
    with open(file_name, 'w') as file:
        file.writelines(output_header)
        for row in image_array:
            for pixel in row:
                file.write(f'{pixel[0]} {pixel[1]} {pixel[2]}\n')


                
                
def ppmFileRead(fileName):
    img_header = []   # Placeholder 
    img = np.array([])   # Placeholder

    with open(fileName, 'rb') as file:
        for line in file:
            line = line.strip().decode()

            if not line.startswith('#'):
                img_header.append(line + "\n")
                
                # If we have collected 3 lines (header lines), break
                if len(img_header) == 3:
                    break

        dimensions = img_header[1].strip().split()
        width, height = map(int, dimensions)

        # Read pixel data
        pixels = np.fromfile(file, dtype=np.uint8, count=width*height*3)
        img = pixels.reshape((height, width, 3))

    print(f"Image Dimensions: {width} x {height}")

    return img_header, img


            
def max_pooling(input_array, pool_size):
    height, width = input_array.shape
    pool_height, pool_width = pool_size, pool_size

    pooled_height = (height + pool_height - 1) // pool_height
    pooled_width = (width + pool_width - 1) // pool_width

    pooled_array = np.zeros((pooled_height, pooled_width), dtype=input_array.dtype)

    for i in range(pooled_height):
        for j in range(pooled_width):
            start_i = i * pool_height
            end_i = min((i + 1) * pool_height, height)
            start_j = j * pool_width
            end_j = min((j + 1) * pool_width, width)

            pool_region = input_array[start_i:end_i, start_j:end_j]
            max_value = np.max(pool_region)
            pooled_array[i, j] = max_value

    return pooled_array





def oil_painting(input_array, pool_size):
    pool_size = int(pool_size)
    height = input_array.shape[0]
    width = input_array.shape[1]
    
    oil_painted_image = np.zeros((height, width), dtype=int)

    for current_row in range(height):
        for current_col in range(width):
            row_start = current_row
            row_end = row_start + pool_size
            col_start = current_col
            col_end = col_start + pool_size
            block = input_array[row_start:row_end, col_start:col_end]

            if np.any(block):
                median_value = np.nanmedian(block).astype(int)
                oil_painted_image[current_row, current_col] = median_value
            else:
                oil_painted_image[current_row, current_col] = 0 

    return oil_painted_image




def main():
    imgFileName, poolSize, part = sys.argv[1:]
    header, image = pgmFileRead(imgFileName)

    poolSize = int(poolSize)

    if part == '1':
        pooled_image = max_pooling(image, (poolSize, poolSize))
        image_save(header, pooled_image, f"{imgFileName[:-4]}_pooled_{poolSize}.pgm")
    elif part == '2':
        oil_painted_image = oil_painting(image, poolSize)
        image_save(header, oil_painted_image, f"{imgFileName[:-4]}_oil_painted_{poolSize}.pgm")
    elif part == '3':
        header, image_data = ppmFileRead(imgFileName)
        painted_data = oil_painting(image_data, poolSize)
        output_filename = f"{base_name}_oil_painted_{poolSize}.ppm"  
        ppmFileSave(header, painted_data, output_filename)
    else:
        print(f'Invalid part argument: {part}. Please use "1" for max pooling or "2" for oil painting or "3" for oil painting (colored).')

if __name__ == '__main__':
    main()