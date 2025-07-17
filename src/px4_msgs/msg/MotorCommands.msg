uint64 timestamp        # 时间戳 (microseconds)
float32[4] commands    # 4个电机的标准化命令 (0.0-1.0)
uint8 source           # 命令来源 (0:未知, 1:ROS, 2:遥控器)