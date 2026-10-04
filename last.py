peserta = [
    {"nama": "Ani", "aktif": True, "nilai": 80, "kehadiran": 90,
     "sanksi": False, "teknologi": {"Python"}},
    {"nama": "Budi", "aktif": True, "nilai": 59, "kehadiran": 88,
     "sanksi": False, "teknologi": {"SQL"}},
    {"nama": "Citra", "aktif": True, "nilai": 75, "kehadiran": 75,
     "sanksi": False, "teknologi": {"Java"}},
    {"nama": "Deni", "aktif": False, "nilai": 90, "kehadiran": 95,
     "sanksi": False, "teknologi": {"Python", "SQL"}},
]

def lolos(data):
    return (
        data["aktif"]
        and data["nilai"] >= 60
        and data["kehadiran"] >= 75
        and not data["sanksi"]
        and bool(data["teknologi"] & {"Python", "SQL"})
    )

for data in peserta:
    print(data["nama"], "lolos" if lolos(data) else "tidak lolos")