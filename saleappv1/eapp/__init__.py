from flask import Flask   # // Dùng để tạo ứng dụng web Flask.
from flask_sqlalchemy import SQLAlchemy #Cho phép thao tác database bằng Python thay vì viết SQL thuần.
from flask_login import LoginManager #Dùng để quản lý đăng nhập, đăng xuất, xác thực người dùng trong ứng dụng web Flask.
import cloudinary #Dùng để upload ảnh lên Cloudinary.

app = Flask(__name__) #Tạo đối tượng Flask.
app.secret_key = '&(^&*^&*^U*HJBJKHJLHKJHK&*%^&5786985646858' #Khóa bí mật để bảo vệ dữ liệu phiên làm việc.
app.config["SQLALCHEMY_DATABASE_URI"] =  "mysql+mysqlconnector://root:12345@localhost/saledb" #Cấu hình kết nối cơ sở dữ liệu.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True #Theo dõi các thay đổi của SQLAlchemy.
app.config["PAGE_SIZE"] = 8 #Số lượng mục hiển thị trên mỗi trang.

db = SQLAlchemy(app=app) #Tạo đối tượng SQLAlchemy.
login = LoginManager(app=app) #Tạo đối tượng LoginManager.

cloudinary.config(cloud_name='dxxwcby8l', #Cấu hình Cloudinary.
api_key='792844686918347',
api_secret='T8ys_Z9zaKSqmKWa4K1RY6DXUJg')
