from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

# Hàm để lấy các liên kết chương truyện từ trang web
def get_comic_links(url):
    driver = webdriver.Firefox()
    driver.get(url)

    comic_links = []

    # Lặp qua các chỉ số li tăng dần lên
    for i in range(1, 100):  # Chỉ số li tăng dần từ 1 đến 100 (hoặc số lớn hơn tùy vào trang web của bạn)
        xpath = f'//*[@id="nt_listchapter"]/nav/ul/li[{i}]/div[1]/a'
        elements = driver.find_elements(By.XPATH, xpath)
        if not elements:
            break

        for element in elements:
            href = element.get_attribute("href")
            if href:
                comic_links.append(href)

    # Đóng trình duyệt
    driver.quit()
    return comic_links

# Hàm để lấy các liên kết ảnh từ trang chương truyện
def get_image_links(comic_links, chapter_number):
    # Khởi tạo trình duyệt Firefox
    driver = webdriver.Firefox()
    driver.set_window_size(400, 400)

    # Mở trang web
    driver.get(comic_links)

    # Số lượng trang bạn muốn lặp qua
    num_pages = 35

    # Danh sách để lưu trữ tất cả các URL hình ảnh
    image_urls = []

    # Lặp qua các trang
    for i in range(1, num_pages + 1):
        # Lấy các phần tử <img> với XPath tương ứng
        img_elements = driver.find_elements(By.XPATH, f'//*[@id="page_{i}"]/img')
        # Lặp qua từng phần tử <img> và lấy thuộc tính 'src'
        for img in img_elements:
            src = img.get_attribute('src')
            if src:
                image_urls.append(src)

    # Đóng trình duyệt sau khi hoàn thành
    driver.quit()

    file_name = f"Chapter {chapter_number}.txt"
    try:
        # Ghi các URL hình ảnh vào tệp văn bản
        with open(file_name, 'w') as file:
            for url in image_urls:
                file.write(url + '\n')
        print(f"Image URLs saved to {file_name}")
    except Exception as e:
        print(f"Error occurred while saving image URLs: {str(e)}")


# URL của trang web chứa các chương truyện
comic_url = input("Nhập URL của trang web chứa truyện: ")
urlSearch = input("Nhập URL tìm kiếm link ảnh: ")
#comic_url = "https://www.nettruyenbb.com/truyen-tranh/du-bao-khai-huyen-100000"
#urlSearch = "//i32.ntcdntempv26.com/data/images/"
comic_links = get_comic_links(comic_url)

if comic_links:
    chapter_number = 1
    for link in reversed(comic_links):
        get_image_links(link, chapter_number)
        chapter_number += 1
else:
    print("Không tìm thấy liên kết truyện trên trang web.")
