# 文件浏览根目录；空或 "/" 表示可浏览到 /，并可「..」到 /
FILEBROWSER_PATH = ""
# 默认起始目录（相对 root）：打开 /files/ 时先进入该目录，如 "mnt" 表示默认 /mnt
FILEBROWSER_DEFAULT_START = ""
# Use tmpfs; JPG written by GUI via stb_image_write, faster encode
REMOTE_SCREEN_PATH = "/dev/shm/remote_screen.jpg"
REMOTE_INPUT_PATH = "/tmp/x6100_remote_ctrl"

# Logbook paths (DATA partition; same as x6100_gui)
FT_LOG_ADI_PATH = "/mnt/ft_log.adi"
INCOMING_LOG_ADI_PATH = "/mnt/incoming_log.adi"
QSO_LOG_DB_PATH = "/mnt/qso_log.db"
# Init script for stop/start around logbook mutations (does not affect boot autostart)
GUI_INIT_SCRIPT = "/etc/init.d/S95gui"
# GUI binary OTA (zip with single member named as content sha256)
GUI_BIN_PATH = "/usr/sbin/x6100_gui"
GUI_OTA_MAX_BYTES = 32 * 1024 * 1024
