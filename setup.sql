CREATE DATABASE QuanLyStore;
GO
USE QuanLyStore;

CREATE TABLE SanPham (
    MaSP INT PRIMARY KEY,
    TenSP NVARCHAR(100),
    Gia FLOAT
);

INSERT INTO SanPham VALUES 
(1, 'Laptop Gaming', 1500), 
(2, 'Chuot Khong Day', 25), 
(3, 'Ban Phim Co', 80),
(4, 'Man Hinh 2K', 300);