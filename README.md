# Tugas UTS Teknik Kompilasi: Mini Compiler

## Identitas Mahasiswa

| Keterangan | Detail |
| :--- | :--- |
| **Nama** | Anshorullah |
| **NIM** | 231011401467 |
| **Kelas** | 06TPLM002 |

---

## Pertanyaan Refleksi & Jawaban

### 1. Hierarki Fungsi dan *Operator Precedence*
**Pertanyaan:**
> Mengapa fungsi `power()` harus dipanggil di dalam `term()`, bukan sebaliknya? Jelaskan kaitannya dengan *Operator Precedence*.

**Jawaban:**
Karena pangkat (`^`) dikerjakan sebelum perkalian/pembagian (`*`, `/`), metode untuk perkalian (`term`) harus mendelegasikan evaluasi awal ke metode pangkat (`power`). Dengan demikian, `power` akan mengonsumsi token secara lebih mengikat (membentuk *node* daun yang lebih dalam pada AST) sebelum operasi perkalian dan pembagian dibentuk. 

Hal ini berkaitan langsung dengan aturan **Prioritas Operator (*Operator Precedence*)**. Dalam konsep *Recursive Descent Parser*, fungsi yang dipanggil lebih dalam secara struktur memiliki prioritas eksekusi yang lebih tinggi.

---

### 2. Analisis Semantik & Variabel Tidak Terdefinisi
**Pertanyaan:**
> Apa yang terjadi pada fase **Analisis Semantik** jika variabel `z` digunakan dalam kode sumber tetapi tidak ada di `symbol_table`?

**Jawaban:**
Program akan melempar pengecualian atau **Exception**. Hal ini karena *compiler* tidak dapat menemukan referensi nilai dari variabel tersebut, sehingga proses kompilasi tidak dapat dilanjutkan.

---

### 3. Urutan Eksekusi *Three-Address Code* (TAC)
**Pertanyaan:**
> Jelaskan mengapa dalam TAC, instruksi untuk `a ^ 2` harus muncul sebelum instruksi untuk `+`.

**Jawaban:**
Pembuatan *Three-Address Code* (TAC) dilakukan dengan menelusuri Pohon Sintaksis Abstrak (AST) menggunakan metode **Post-Order Traversal** (bawah-ke-atas) yang diimplementasikan pada fungsi rekursif `generate_tac`. 

Karena operasi pangkat (`^`) memiliki prioritas lebih tinggi, operasi `a ^ 2` posisinya berada lebih di bawah (sebagai *child node*) dibandingkan operasi penjumlahan `+` (sebagai *parent node*). Oleh karena itu, *child node* harus dievaluasi dan diubah menjadi instruksi TAC terlebih dahulu agar hasilnya bisa digunakan oleh *parent node*.