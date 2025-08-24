import os
import sys
from datetime import datetime

def write_log(problem_id, problem_name, message, level="INFO"):
    # 建立資料夾名稱，例如 "1_two_sum"
    folder_name = f"{problem_id}_{problem_name.replace(' ', '_').lower()}"
    os.makedirs(folder_name, exist_ok=True)  # 如果不存在就建立

    # Log 檔路徑
    log_path = os.path.join(folder_name, "log.txt")

    # 產生 log 格式
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}\n"

    # 寫入 log 檔案
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_line)

    print(f"✅ 已寫入 {log_path}")

def main():
    if len(sys.argv) < 3:
        print("用法: python leetcode_logger.py <題號> <題目名稱>")
        print("例如: python leetcode_logger.py 1 'Two Sum'")
        return

    problem_id = sys.argv[1]
    problem_name = sys.argv[2]

    print(f"📘 正在記錄題目 {problem_id}: {problem_name}")
    print("輸入你的想法（輸入空白行結束）：")

    # 讓使用者輸入多行內容
    lines = []
    while True:
        line = input("> ")
        if line.strip() == "":
            break
        lines.append(line)

    # 合併為一段文字
    if lines:
        message = " ".join(lines)
        write_log(problem_id, problem_name, message, level="INFO")
    else:
        print("⚠️ 沒有輸入任何內容，沒有寫入 log。")

if __name__ == "__main__":
    main()
