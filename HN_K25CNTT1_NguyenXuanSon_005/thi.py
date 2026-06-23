from tabulate import tabulate
class Booking:
    def __init__(self,id,customer_name ,room_number ,room_price ,nights ,service_fee ,discount ):
        self.id = id
        self.customer_name = customer_name
        self.room_number = room_number
        self.room_price = room_price
        self.nights = nights
        self.service_fee = service_fee
        self.discount = discount
        self.total_rent = 0
        self.rent_type = ""

        self.calculate_total_rent()
        self.classify_rent()

    def calculate_total_rent(self):
        self.total_rent = self.room_price * self.nights + self.service_fee - self.discount 
        return self.total_rent

    def classify_rent(self):
        self.calculate_total_rent()

        if self.total_rent < 1000000 :
            self.rent_type = "Tiết kiệm"
        elif self.total_rent < 3000000 :
            self.rent_type = "Tiêu chuẩn"
        elif self.total_rent < 7000000 :
            self.rent_type = "Cao Cấp"
        else:
            self.rent_type = "VIP"

class BookingManager:
    def __init__(self):
        self.bookings = []

    def find_id(self,id):
        for item in self.bookings:
            if item.id == id:
                return item
        return None

    def add_booking(self):
        while True:
            id = input("Mã đặt phòng: ").strip()

            if not id : 
                print("Mã đặt phòng không được rỗng")
                continue
            elif self.find_id(id):
                print("Mã đặt phòng không được trùng")
                continue
            break

        while True:
            customer_name = input("Họ tên khách hàng: ").strip()

            if not customer_name:
                print("Họ tên khách hàng không được rỗng")
                continue
            break

        while True:
            room_number = input("Số phòng: ").strip()

            if not room_number :
                print("Số phòng không được rỗng")
                continue
            break
           
        while True :
            try:
                room_price = float(input("Giá phòng một đêm: ").strip())

                if room_price < 0 :
                    print("Giá phòng một đêm phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Nhập số nguyên")

        while True:
            try :
                nights = int(input("Số đêm thuê: ").strip())

                if nights < 1 or nights > 365:
                    print("Số đêm thuê phải là số nguyên từ 1 đến 365")
                    continue
                break
            except ValueError: 
                print("Số đêm thuê phải là số nguyên từ 1 đến 365")
        while True:
            try:
                service_fee = float(input("Phụ phí dịch vụ: ").strip())

                if service_fee < 0:
                    print("Phụ phí dịch vụ phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Phí dịch vụ phải nhập là số!")

        while True:
            try:
                discount = float(input("Giảm giá: ").strip())

                if discount < 0:
                    print("Giảm giá phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Giảm giá phải nhập số!")

        booking = Booking(id,customer_name ,room_number ,room_price ,nights ,service_fee ,discount )
        self.bookings.append(booking)
        print("Thêm đặt phòng thành công!")
        
    def show_all(self):
        if not self.bookings:
            print("Danh sách đặt phòng đang rỗng!")
            return
        print("---Danh sách đặt phòng---")
        data= []
        for booking in self.bookings:
            data.append([
                booking.id,
                booking.customer_name,
                booking.room_number,
                booking.room_price,
                booking.nights,
                booking.service_fee,
                booking.discount,
                booking.total_rent,
                booking.rent_type,
            ])
        print(tabulate(data,headers=["Mã đặt phòng","Họ tên khách hàng","Số phòng","Giá phòng một đêm","Số đêm thuê","Phụ phí dịch vụ","Giảm giá","Tổng tiền thuê","Phân loại tiền thuê"],tablefmt="simple"))

    def delete_booking(self):
        new_id = input("Nhập mã đặt phòng cần xóa: ").strip()

        booking = self.find_id(new_id)

        if not booking:
            print(" Không tìm thấy đặt phòng cần xóa!")
            return
        
        choice = input("Bạn có chắc muốn xóa đặt phòng này không? (Y/N): ").strip().lower()

        if choice == "y":
            self.bookings.remove(booking)
            print("Xóa đặt phòng thành công!")
        elif choice == "n":
            print("Đã hủy thao tác xóa!")
        else:
            print("Lựa chọn không hợp lệ")

    def update_booking(self):
        new_id = input("Nhập mã đặt phòng cần cập nhật: ").strip()

        booking = self.find_id(new_id)

        if not booking:
            print(" Không tìm thấy đặt phòng cần cập nhật!")
            return
        
        while True :
            try:
                room_price = float(input("Giá phòng một đêm: ").strip())

                if room_price < 0 :
                    print("Giá phòng một đêm phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Nhập số nguyên")

        while True:
            try :
                nights = int(input("Số đêm thuê: ").strip())

                if nights < 1 or nights > 365:
                    print("Số đêm thuê phải là số nguyên từ 1 đến 365")
                    continue
                break
            except ValueError: 
                print("Số đêm thuê phải là số nguyên từ 1 đến 365")
        while True:
            try:
                service_fee = float(input("Phụ phí dịch vụ: ").strip())

                if service_fee < 0:
                    print("Phụ phí dịch vụ phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Phí dịch vụ phải nhập là số!")

        while True:
            try:
                discount = float(input("Giảm giá: ").strip())

                if discount < 0:
                    print("Giảm giá phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError:
                print("Giảm giá phải nhập số!")

        booking.room_price = room_price
        booking.nights = nights
        booking.service_fee = service_fee
        booking.discount = discount

        booking.calculate_total_rent()
        booking.classify_rent()

        print(" Cập nhật đặt phòng thành công!")

    def search_booking(self):
        pass

manager = BookingManager()
while True:
    print("""
================ MENU ================
1. Hiển thị danh sách đặt phòng
2. Thêm đặt phòng mới
3. Cập nhật đặt phòng
4. Xóa đặt phòng
5. Tìm kiếm đặt phòng
6. Thoát
=====================================

""")
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        manager.show_all()
    elif choice == "2":
        manager.add_booking()
    elif choice == "3":
        manager.update_booking()
    elif choice == "4":
        manager.delete_booking()
    elif choice == "5":
        pass
    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống quản lý đặt phòng khách sạn!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
