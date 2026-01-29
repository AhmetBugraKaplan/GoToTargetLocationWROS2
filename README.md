# 🐢 ROS2 Turtlesim Kontrol Paketleri

ROS2 Humble ile turtlesim robot kontrolü.

## Kurulum
```bash
cd ~/turtlesim_ws/src
git clone https://github.com/AhmetBugraKaplan/GoToTargetLocationWROS2.git
cd ~/turtlesim_ws
colcon build
source install/setup.bash
```

## Kullanım

### 1. Hedef Takibi (Kare Çizer)
```bash
# Terminal 1
ros2 run turtlesim turtlesim_node

# Terminal 2
ros2 run turtlesim_py_pkg go_to_loc
```

### 2. Hız Kontrolü (Daire Çizer)
```bash
# Terminal 1
ros2 run turtlesim turtlesim_node

# Terminal 2 - ros2 run turtlesim_py_pkg vel_controller [hız] [yarıçap]
ros2 run turtlesim_py_pkg vel_controller 2.0 1.0
```

## Özellikler

- **go_to_loc.py**: Belirlenen koordinatlara sırayla gider (2,2) → (8,2) → (8,8) → (2,8)
- **vel_controller.py**: Verilen hız ve yarıçapa göre dairesel hareket

---

**Geliştirici:** Ahmet Buğra Kaplan
