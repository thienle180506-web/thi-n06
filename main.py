import pandas as pd
import gradio as gr
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. DỮ LIỆU HỆ THỐNG
du_lieu_he_thong = [
    [1, 'Laptop Gaming', 1500, 10],
    [2, 'Chuột Không Dây', 25, 50],
    [3, 'Bàn Phím Cơ', 80, 30],
    [4, 'Màn Hình 2K', 300, 15]
]

# 2. LOGIC XỬ LÝ
def xem_du_lieu():
    return pd.DataFrame(du_lieu_he_thong, columns=['Mã SP', 'Tên Sản Phẩm', 'Giá ($)', 'Số lượng tồn'])

def them_san_pham(ma, ten, gia, sl):
    du_lieu_he_thong.append([int(ma), ten, float(gia), int(sl)])
    return xem_du_lieu(), f"✅ Đã thêm: {ten}"

def xoa_san_pham(ma_xoa):
    global du_lieu_he_thong
    du_lieu_he_thong = [item for item in du_lieu_he_thong if item[0] != int(ma_xoa)]
    return xem_du_lieu(), f"🗑️ Đã xóa Mã SP: {ma_xoa}"

def du_bao_doanh_thu(so_luong):
    X = np.array([[10], [20], [30], [50], [100]])
    y = np.array([1000, 2000, 3000, 5000, 10000])
    model = LinearRegression().fit(X, y)
    ket_qua = model.predict([[so_luong]])
    return f"📈 Doanh thu dự kiến: ${ket_qua[0]:.2f}"

# 3. GIAO DIỆN
with gr.Blocks() as demo:
    gr.Markdown("# 🚀 HỆ THỐNG QUẢN LÝ DỮ LIỆU & DỰ BÁO AI")
    gr.Markdown("Sinh viên thực hiện: **Lê Đức Thiện**")
    
    with gr.Tab("📦 Quản lý Sản phẩm"):
        with gr.Row():
            with gr.Column():
                ma_in = gr.Number(label="Mã SP")
                ten_in = gr.Textbox(label="Tên SP")
                gia_in = gr.Number(label="Giá")
                sl_in = gr.Number(label="Số lượng")
                btn_add = gr.Button("➕ Thêm", variant="primary")
            with gr.Column():
                ma_del = gr.Number(label="Mã cần xóa")
                btn_del = gr.Button("🗑️ Xóa", variant="stop")
        table_out = gr.Dataframe(value=xem_du_lieu())
        msg = gr.Textbox(label="Thông báo")
        btn_add.click(them_san_pham, inputs=[ma_in, ten_in, gia_in, sl_in], outputs=[table_out, msg])
        btn_del.click(xoa_san_pham, inputs=ma_del, outputs=[table_out, msg])
        
    with gr.Tab("🤖 Dự báo AI"):
        num_in = gr.Number(label="Số lượng dự kiến")
        btn_pre = gr.Button("Chạy AI")
        txt_out = gr.Textbox(label="Kết quả")
        btn_pre.click(du_bao_doanh_thu, inputs=num_in, outputs=txt_out)

demo.launch()