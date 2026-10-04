python = {"Ani", "Budi", "Citra"}
java = {"Budi", "Deni"}
sql = {"Ani", "Deni", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar"}

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
tidak_menyukai_ketiganya = semua_mahasiswa - (python | java | sql)

print("python saja:", python_saja)
print("python dana java:", python_dan_java)
print("minimal satu teknologi:", minimal_satu)
print("Tidak menuyukai ketiganya:", tidak_menyukai_ketiganya)