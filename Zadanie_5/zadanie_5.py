from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import os

try:
    import cv2
    import numpy as np
    opencv_available = True
except ImportError:
    print("OpenCV nie jest dostępne. Uruchomione zostaną tylko przykłady Pillow.")
    opencv_available = False

def create_directories():
    os.makedirs('pillow_results', exist_ok=True)
    if opencv_available:
        os.makedirs('opencv_results', exist_ok=True)

def pillow_examples():
    print("=== PILLOW EXAMPLES ===")
    
    def resize_image():
        img = Image.new('RGB', (400, 300), color='blue')
        resized = img.resize((200, 150))
        resized.save('pillow_results/resized_image.jpg')
        print("Obraz zmieniony na rozmiar 200x150")

    def apply_filters():
        img = Image.new('RGB', (300, 300), color='white')
        draw = ImageDraw.Draw(img)
        draw.rectangle([50, 50, 250, 250], fill='black')
        draw.ellipse([100, 100, 200, 200], fill='white')
        img.save('pillow_results/original_pattern.jpg')
        
        blurred = img.filter(ImageFilter.BLUR)
        blurred.save('pillow_results/blurred_image.jpg')
        
        sharpened = img.filter(ImageFilter.SHARPEN)
        sharpened.save('pillow_results/sharpened_image.jpg')
        
        print("Zastosowano filtry rozmycia i wyostrzenia")

    def enhance_image():
        img = Image.new('RGB', (250, 250), color=(100, 100, 100))
        draw = ImageDraw.Draw(img)
        draw.rectangle([25, 25, 225, 225], fill=(150, 150, 150))
        draw.ellipse([75, 75, 175, 175], fill=(200, 200, 200))
        img.save('pillow_results/original_gray.jpg')
        
        enhancer = ImageEnhance.Brightness(img)
        bright_img = enhancer.enhance(2.0)
        bright_img.save('pillow_results/bright_image.jpg')
        
        contrast_enhancer = ImageEnhance.Contrast(img)
        contrast_img = contrast_enhancer.enhance(3.0)
        contrast_img.save('pillow_results/contrast_image.jpg')
        
        print("Zwiększono jasność i kontrast obrazu")
    
    resize_image()
    apply_filters()
    enhance_image()
    print("Wszystkie operacje Pillow wykonane pomyślnie")

def opencv_examples():
    if not opencv_available:
        return
    
    print("\n=== OPENCV EXAMPLES ===")
    
    def create_and_save_image():
        img = np.zeros((300, 400, 3), dtype=np.uint8)
        img[:] = (100, 150, 200)
        cv2.imwrite('opencv_results/opencv_base.jpg', img)
        print("Utworzono podstawowy obraz")

    def detect_edges():
        img = np.zeros((200, 200, 3), dtype=np.uint8)
        cv2.rectangle(img, (30, 30), (80, 80), (255, 255, 255), -1)
        cv2.rectangle(img, (120, 120), (170, 170), (255, 255, 255), -1)
        cv2.circle(img, (100, 60), 25, (255, 255, 255), -1)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        
        cv2.imwrite('opencv_results/original_pattern.jpg', img)
        cv2.imwrite('opencv_results/edges_detected.jpg', edges)
        print("Wykryto krawędzie w obrazie")

    def geometric_transformations():
        img = np.zeros((200, 300, 3), dtype=np.uint8)
        cv2.rectangle(img, (50, 50), (150, 100), (0, 255, 0), -1)
        cv2.rectangle(img, (100, 120), (200, 170), (255, 0, 0), -1)
        cv2.putText(img, 'TEST', (80, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        rows, cols = img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
        rotated = cv2.warpAffine(img, rotation_matrix, (cols, rows))
        
        cv2.imwrite('opencv_results/original_shapes.jpg', img)
        cv2.imwrite('opencv_results/rotated_shapes.jpg', rotated)
        print("Wykonano rotację obrazu o 45 stopni")
    
    create_and_save_image()
    detect_edges()
    geometric_transformations()
    print("Wszystkie operacje OpenCV wykonane pomyślnie")

if __name__ == "__main__":
    create_directories()
    pillow_examples()
    opencv_examples()
    
    if opencv_available:
        print("\n=== PODSUMOWANIE ===")
        print("Wszystkie przykłady wykonane pomyślnie!")
        print("Wyniki Pillow: pillow_results/")
        print("Wyniki OpenCV: opencv_results/")
    else:
        print("\n=== PODSUMOWANIE ===")
        print("Przykłady Pillow wykonane pomyślnie!")
        print("Wyniki Pillow: pillow_results/")
        print("Aby uruchomić przykłady OpenCV, zainstaluj: pip install opencv-python")