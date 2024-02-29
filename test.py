from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt
driver = webdriver.Firefox()

# Mở trang web
driver.get("URL_của_trang_web")

# Khởi tạo danh sách chứa các liên kết
links = []

# Lặp qua các chỉ số li tăng dần lên
for i in range(1, 100):  # Chỉ số li tăng dần từ 1 đến 100 (hoặc số lớn hơn tùy vào trang web của bạn)
    xpath = f'//*[@id="nt_listchapter"]/nav/ul/li[{i}]/div[1]/a'
    elements = driver.find_elements(By.XPATH, xpath)
    if not elements:
        break

    for element in elements:
        href = element.get_attribute("href")
        if href:
            links.append(href)

# In ra các liên kết đã tìm thấy
for link in links:
    print(link)

# Đóng trình duyệt
driver.quit()
