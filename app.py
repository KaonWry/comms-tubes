# Modules
from crypt import methods
from curses.ascii import islower
from os import getlogin, write
import os
import time
import datetime
from datetime import date, timedelta
import sys
import locale
from flask import Flask, request, render_template, Markup

# Set locale
locale.setlocale(locale.LC_ALL, '')

# Flask constructor
app = Flask(__name__)  


# Jadwal kegiatan
Kalender = ["Tidak ada agenda khusus"] * 730
Kalender[55] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[56] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[57] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[58] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[59] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[60] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[61] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[62] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[63] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[64] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[65] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[66] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[67] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[68] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[69] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[70] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2022/2023 oleh Program Studi'
Kalender[217] ='Batas Akhir Pengajuan Perpanjangan Waktu Studi dari mahasiswa'
Kalender[221] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[222] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[223] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[224] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[225] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[226] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[227] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[228] ='Perwalian dan Pendaftaran Ulang Semester I-2022/2023 Bagi Seluruh Mahasiswa'
Kalender[233] ='Batas Waktu Pembayaran Biaya Pendidikan Semester I-2022/2023 bagi Mahasiswa Lama'
Kalender[234] ='Hari Pertama Masa Kuliah Semester I-2022/20223 & Batas Akhir Perubahan Nilai Mata Kuliah KP/TA/Tesis/Disertasi Semester I-2021/2022 '
Kalender[249] ='Yudisium ITB Bulan September 2022'
Kalender[252] ='Batas Akhir Perubahan Nilai Mata Kuliah Bukan KP/TA/Tesis/Disertasi Semester II-2021/2022 dan Semester Pendek 2021/2022'
Kalender[256] ='Penggantian Rencana Studi Semester I-2022/2023'
Kalender[257] ='Penggantian Rencana Studi Semester I-2022/2023'
Kalender[258] ='Penggantian Rencana Studi Semester I-2022/2023'
Kalender[259] ='Penggantian Rencana Studi Semester I-2022/2023'
Kalender[262] ='Penyelesaian Kasus Mahasiswa yang Tidak Mendaftar Dua Semester'
Kalender[271] ='Batas Waktu Pemenuhan Persyaratan Administrasi Kelulusan dan Pendaftaran Seremoni Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[277] ='Yudisium ITB Bulan Oktober 2022'
Kalender[278] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[279] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[280] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[281] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[282] ='Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[283] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[284] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[285] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[286] ='Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[287] =' Batas Waktu Pemasukan Nilai MBKM Semester II-2021/2022 & Masa Ujian Tengah Semester I-2022/2022 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[289] ='Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[290] ='Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi & Pengisian Kuesioner Wisuda Pertama Tahun Akademik 2022/2023'
Kalender[291] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[292] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[293] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[294] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[295] =' Hari Wisuda Pertama Tahun Akademik 2022/2023 & Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[296] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[297] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[298] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[299] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[300] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[301] =' Periode Pembukaan Kelas/Mata Kuliah Semester II-2022/2023 oleh Program Studi '
Kalender[305] ='Yudisium ITB Bulan November 2022'
Kalender[321] ='Batas Koreksi DPK untuk Acuan DNA Semester I-2022/2023'
Kalender[332] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[333] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[334] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[335] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[336] ='Hari Terakhir Masa Kuliah Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[337] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[338] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[339] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[340] ='Ujian Akhir Semester I-2022/2023 & Yudisium ITB Bulan Desember 2022 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[341] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[342] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[343] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[344] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[345] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[346] ='Ujian Akhir Semester I-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester I-2022/2023'
Kalender[347] ='Ujian Akhir Semester I-2022/2023'
Kalender[348] ='Ujian Akhir Semester I-2022/2023'
Kalender[349] ='Ujian Akhir Semester I-2022/2023'
Kalender[350] ='Ujian Akhir Semester I-2022/2023'
Kalender[351] ='Ujian Akhir Semester I-2022/2023'
Kalender[352] ='Ujian Akhir Semester I-2022/2023'
Kalender[353] ='Ujian Akhir Semester I-2022/2023'
Kalender[354] ='Ujian Akhir Semester I-2022/2023'
Kalender[356] ='Batas Akhir Pengajuan Perpanjangan Waktu Studi dari mahasiswa '
Kalender[368] ='Yudisium ITB Bulan Januari 2023'
Kalender[369] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa & Penyelesaian Kasus Batas Waktu Studi untuk Mahasiswa Yang Mendaftar di Semester Genap'
Kalender[370] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
Kalender[371] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
Kalender[372] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
Kalender[373] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
Kalender[374] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
Kalender[375] ='Perwalian dan Pendaftaran Ulang Semester II-2022/2023 bagi Seluruh Mahasiswa'
Kalender[377] ='Sidang Terbuka ITB Dalam Rangka Penerimaan Seluruh Mahasiswa Baru Semester Genap'
Kalender[380] ='Batas Waktu Pembayaran Biaya Pendidikan Semester II-2022/2023'
Kalender[381] ='Hari Pertama Masa Kuliah Semester II-2022/2023 & Batas Akhir Perubahan Nilai Mata Kuliah KP/TA/Tesis/Disertasi Semester II-2021/2022 dan Semester Pendek 2021/2022'
Kalender[395] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[396] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[397] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[398] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[399] ='Batas Akhir Perubahan Nilai Mata Kuliah Bukan KP/TA/Tesis/Disertasi Semester I-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
Kalender[400] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[401] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[402] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[403] ='Penggantian Rencana Studi Semester II-2022/2023 & Yudisium ITB Bulan Februari 2023 & Verifikasi Portofolio Semester I-2022/2023'
Kalender[404] ='Penggantian Rencana Studi Semester II-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
Kalender[405] ='Penggantian Rencana Studi Semester II-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
Kalender[406] ='Penggantian Rencana Studi Semester II-2022/2023 & Verifikasi Portofolio Semester I-2022/2023'
Kalender[407] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[408] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[409] ='Penyelesaian Kasus Mahasiswa yang Tidak Mendaftar Dua Semester & Verifikasi Portofolio Semester I-2022/2023'
Kalender[410] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[411] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[412] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[413] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[414] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[415] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[416] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[417] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[418] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[419] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[420] ='Verifikasi Portofolio Semester I-2022/2023'
Kalender[426] ='Sidang Terbuka Dalam Rangka Dies Natalis ke-64 ITB'
Kalender[430] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
Kalender[431] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Yudisium ITB Bulan Maret 2023 & Masa Ujian Tengah Semester II-2022/2023'
Kalender[432] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
Kalender[433] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
Kalender[434] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi & Masa Ujian Tengah Semester II-2022/2023'
Kalender[435] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[436] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[437] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[438] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[439] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[439] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[440] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[441] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[442] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[443] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[444] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[445] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[446] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[447] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[448] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[449] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[450] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[451] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[452] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[453] ='Batas Waktu Pemenuhan Persyaratan Administrasi Kelulusan dan Pendaftaran Seremoni Wisuda Kedua Tahun Akademik 2022/2023Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[454] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[455] ='Periode Pembukaan Kelas/Mata Kuliah Semester I-2023/2024 oleh Program Studi'
Kalender[456] ='Yudisium ITB Bulan April 2023'
Kalender[474] ='Batas Koreksi DPK untuk Acuan DNA Semester II-2022/2023'
Kalender[460] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[461] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[462] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[463] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[464] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[465] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[466] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[467] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[468] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[469] ='Batas Waktu Pemasukan Nilai MBKM Semester I-2022/2023 & Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[470] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[471] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[472] ='Pengisian Kuesioner Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[474] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[475] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[476] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[477] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[478] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[479] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[480] ='Libur Kuliah dalam rangka Idul Fitri'
Kalender[483] ='Batas Akhir Pemilihan untuk Mahasiswa Berprestasi Tingkat Fakultas/Sekolah'
Kalender[484] ='Hari Wisuda Kedua Tahun Akademik 2022/2023'
Kalender[487] ='Yudisium ITB Bulan Mei 2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[488] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[489] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[490] ='Hari Terakhir Masa Kuliah Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[491] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[492] ='Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[493] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[494] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[495] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[496] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[497] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[498] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[499] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[500] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[501] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[502] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[503] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[504] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[505] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[506] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[507] ='Ujian Akhir Semester II-2022/2023 & Pengisian Kuesioner Evaluasi Perkuliahan Semester II-2022/2023'
Kalender[508] ='Ujian Akhir Semester II-2022/2023'
Kalender[522] ='Yudisium ITB Bulan Juni 2023 & Batas Akhir Pemasukan Nilai Mata Kuliah Semester II-2022/2023'
Kalender[523] ='Batas Akhir Pengisian Kuesioner Akhir Pilihan Program Studi Mahasiswa TPB 2023'
Kalender[529] ='Penjurusan Mahasiswa TPB 2023'
Kalender[612] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[613] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[614] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[615] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[616] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[617] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[618] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[619] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[620] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[621] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[622] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[623] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[624] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[625] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[626] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[627] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[628] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[629] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[630] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[631] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[632] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[633] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[634] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[635] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[636] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[637] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[638] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[639] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[640] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[641] ='Verifikasi Portofolio Semester II-2022/2023'
Kalender[642] ='Verifikasi Portofolio Semester II-2022/2023'





# Program startup
@app.route("/")
def startup():
    if (os.path.isfile("session.txt")):
        os.remove("session.txt")
    return render_template("index.html")

# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    isLogin = False
    # Import NIM
    importData = open("dataKelas02.txt", "r")
    importData = importData.read()
    importData = (importData.split("\n"))
    dataNIM = [0] * len(importData)
    dataNama = [0] * len(importData)
    j = 0
    for i in importData:
        i = i.split("-")
        dataNama[j] = i[1]
        dataNIM[j] = i[0]
        j += 1
    inpNIM = request.form.get("NIM")
    # Input
    if (inpNIM in dataNIM):
        nama = dataNama[dataNIM.index(inpNIM)]
        isLogin = True
    else:
        nama = ""
        isLogin = False
    f = open("session.txt", "w")
    f = f.write(f"{nama}\n{inpNIM}\n{isLogin}")
    # Output
    if (request.method == "POST"):
        return render_template("index.html", nama = nama, isLogin = isLogin)
    else:
        return render_template("index.html")


# Kalender
@app.route("/jadwal", methods=["POST", "GET"])
def kalender():
    f = open("session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    inpNIM = f[1]
    isLogin = f[2]
    tanggal = request.form.get("tanggal")
    tanggal = int(time.mktime(datetime.datetime.strptime(tanggal, "%m/%d/%Y").timetuple()))
    tanggalAwal = int(datetime.datetime(2022, 1, 1).timestamp())
    tanggalSekarang = ((tanggal - tanggalAwal)/(60*60*24))
    tanggalSekarang = int(tanggalSekarang)
    jadwalHariIni = Kalender[tanggalSekarang]
    # Output
    if (request.method == "POST"):
        return render_template("index.html", tanggal = tanggal, isLogin = isLogin, jadwalHariIni = jadwalHariIni, nama = nama)
    else:
        return render_template("index.html")

# Petunjuk arah
@app.route("/rute", methods=["POST", "GET"])
def rute():
    f = open("session.txt")
    f = f.read()
    f = f.split("\n")
    nama = f[0]
    inpNIM = f[1]
    isLogin = f[2]
    hari = request.form.get("hari")
    gerbang = int(request.form.get("pintuMasuk"))
    jadwal = int(request.form.get("jampel"))
    minggu = request.form.get("minggu")
    def readRoute(txt, jadwal, gerbang):
        inpRead = (open(txt).read()).split("\n\n\n")
        for i in range(len(inpRead)):
            inpRead[i] = list((inpRead[i]).split("\n\n"))
        return (inpRead[jadwal-1])[gerbang-1]

    if (hari == "1"):
        bukaHari = "arahSenin.txt"
    elif (hari == "2"):
        if (minggu == "a"):
            bukaHari = "arahSelasaA.txt"
        elif (minggu == "b"):
            bukaHari = "arahSelasaB.txt"
    elif (hari == "3"):
        bukaHari = "arahRabu.txt"
    elif (hari == "4"):
        bukaHari = "arahKamis.txt"
    elif (hari == "5"):
        bukaHari = "arahJumat.txt"
    
    if (hari in ["6", "7"]):
        ruteJalan = "Hari ini libur\nYey:)"
    else:
        jumlahJam = int(len((open(bukaHari).read()).split("\n\n\n"))) + 1
        if(jumlahJam > jadwal):
            ruteJalan = readRoute(bukaHari, jadwal, gerbang)
        else:
            ruteJalan = "Tidak ada kuliah onsite jam segitu"

    
    # ruteJalan = ruteJalan.replace("\n", "<br>")
    if (request.method == "POST"):
        return render_template("index.html", nama = nama, ruteJalan = ruteJalan, isLogin = isLogin)
    else:
        return render_template("index.html")
    
    
    
if __name__=='__main__':
    app.run(debug=True)