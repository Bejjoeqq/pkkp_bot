-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 21 Jan 2021 pada 15.47
-- Versi Server: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pkkp`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `pkkp_admin`
--

CREATE TABLE `pkkp_admin` (
  `admin_id` int(11) NOT NULL,
  `admin_username` varchar(255) NOT NULL,
  `admin_password` varchar(255) NOT NULL,
  `admin_level` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pkkp_admin`
--

INSERT INTO `pkkp_admin` (`admin_id`, `admin_username`, `admin_password`, `admin_level`) VALUES
(2, 'bejjo', '8e4ef73117969fe1df8c327825239256', 1),
(3, 'aldi', 'daf036f7f77e11a342e9520ff8fc256d', 1),
(4, 'fradanan', 'ce27df5006096107f8c0b1a31dbb1912', 3),
(8, 'haqi', 'c13da60df716606a2e696a5faa0268c6', 3),
(9, 'bila', '177826b3d748ab6ac46d226326779a3d', 3),
(10, 'admin', 'd9da8170e8bc9f27b2d32a6c9a6c697d', 2),
(11, 'umum', 'f5df3bde70b7b7ab67ce0e00edcb1951', 3),
(12, 'content', '9a0364b9e99bb480dd25e1f0284c8555', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pkkp_berita`
--

CREATE TABLE `pkkp_berita` (
  `berita_id` int(11) NOT NULL,
  `berita_judul` varchar(100) NOT NULL,
  `berita_text` varchar(3900) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pkkp_berita`
--

INSERT INTO `pkkp_berita` (`berita_id`, `berita_judul`, `berita_text`) VALUES
(2, 'Gelar Program PKKP, Disporapar Jateng Butuh 200 Sarjana', 'Semarang, Gatra.com - Dinas Kepemudaan, Olahraga dan Pariwisata (Disporapar) Jawa Tengah membutuhkan 200 orang lulusan sarjana (S1) segala jurusan. Mereka akan ditugaskan di sejumlah desa dalam rangka program Pengembangan Kepedulian dan Kepeloporan Pemuda (PKKP) 2019. Kepala Seksi Pengembangan Kepemudaan Disporapar Jawa Tengah (Jateng) P. Bono Listiyanto, mengatakan masa kontrak kerja peserta program PKKP selama 10 bulan yakni Maret-Desember 2019. ï¿½Ke-200 peserta program PKKP akan ditempatkan di 100 desa tersebar di 15 kabupaten,ï¿½ katanya kepada Gatra.com di Semarang, Rabu (23/1). Ke-15 kabupaten itu masing-masing Brebes, Pemalang, Banyumas, Cilacap, Kebumen, Demak, Klaten, Banjarnegara, Grobogan, Purworejo, Sragen, Purbalingga, Rembang, Wonosobo, dan Blora. Tugas peserta program PKKP, lanjut Bono, sebagai motivator, fasilitator, akselerator, dinamisator, dan penggerak ekonomi mandiri masyarakat desa, terutama para pemuda desa. ï¿½Seleksi penerimaan program PKKP 2019 tak dipungut biaya atau gratis,ï¿½ tandasnya. Staf Seksi Pengembangan Kepemudaan Disporapar Jateng, Surya Wijaya, menjelaskan pendaftaran program PKKP pada 28-30 Januari 2019. Persyaratan pendaftaran antara lain, penduduk Jateng, usia maksimal 28 tahun pada 1 Maret 2019, indeks prestasi kumulatif (IPK) 2,75, belum menikah, mempunyai kemampuan menulis dan mendokumentasikan laporan melalui teknologi informasi (internet) ï¿½Pendaftaran dilakukan secara online melalui wabsite disporapar.jatengprov.go.id,ï¿½ ujar Surya. Menurut dia, disediakan kuota 10% atau 20 orang bagi penyandang disabilitas dengan catatan tidak mengganggu aktivitas sehari-hari dan dapat melakukan pekerjaan. ï¿½Peserta yang dinyatakan lulus seleksi administrasi selanjutnya mengikuti seleksi tertulis dan wawancara yang digelar di Badan Diklat BKK Jateng di Semarang pada 12-14 Februari mendatang,ï¿½ ujar dia.'),
(9, 'Tambahkan Berita Melalui Admin Panel', 'Login sebagai content di Admin Panel\r\nUsername : content\r\nPassword : content');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pkkp_daftar`
--

CREATE TABLE `pkkp_daftar` (
  `daftar_idtele` int(11) NOT NULL,
  `daftar_nama` varchar(255) DEFAULT NULL,
  `daftar_email` varchar(255) DEFAULT NULL,
  `daftar_jk` varchar(10) DEFAULT NULL,
  `daftar_foto` varchar(50) DEFAULT NULL,
  `daftar_fotoid` varchar(255) DEFAULT NULL,
  `daftar_status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pkkp_daftar`
--

INSERT INTO `pkkp_daftar` (`daftar_idtele`, `daftar_nama`, `daftar_email`, `daftar_jk`, `daftar_foto`, `daftar_fotoid`, `daftar_status`) VALUES
(101010, 'test', 'test@test.com', 'test', '', '', 'tidak'),
(948159175, 'Bejjo Eqq', 'bejjoeqq@gmail.com', 'Laki-Laki', '948159175.png', 'AgACAgUAAxkBAAICG2AFBLM023aNXAqroC2QWJPOUKcZAAKwqjEbR7EoVPr-J5H9-zKsh0Crb3QAAwEAAwIAA3gAAyBOAAIeBA', 'ya'),
(1309620134, 'Aldhiya Rozak', 'aldhiya.rozak@gmail.com', 'Laki-Laki', '1309620134.png', 'AgACAgUAAxkBAAIBu2AEIawaSSQ829W81bo1LwHnwKDlAAJOqjEb7w0hVKZfFSXUPJZSSAKxbnQAAwEAAwIAA3gAA15wAQABHgQ', 'ya');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pkkp_history`
--

CREATE TABLE `pkkp_history` (
  `history_id` int(11) NOT NULL,
  `history_chat` varchar(4100) NOT NULL,
  `daftar_idtele` int(11) NOT NULL,
  `key_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pkkp_history`
--

INSERT INTO `pkkp_history` (`history_id`, `history_chat`, `daftar_idtele`, `key_id`) VALUES
(2, '/start', 1309620134, 1),
(3, '/start', 1309620134, 1),
(4, '/bantuan', 1309620134, 4),
(5, '/hey', 1309620134, 2),
(6, '/tolong', 1309620134, 3),
(7, '/saran', 1309620134, 5),
(8, '/saran isi pesan', 1309620134, 5),
(9, '/info', 1309620134, 6),
(10, '/daftar', 1309620134, 7),
(11, '/foto', 1309620134, 8),
(12, '/foto', 1309620134, 8),
(13, '/hasil', 1309620134, 9),
(14, '/materi', 1309620134, 10),
(15, '/pembekalan', 1309620134, 11),
(16, '/syarat', 1309620134, 12),
(17, 'ty', 1309620134, 13),
(18, 'thanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanksthanks', 1309620134, 13),
(19, 'https://t.me/pkkpdisporapar_bot', 1309620134, 13),
(20, '/berita', 1309620134, 14),
(21, '/berita', 1309620134, 14),
(22, '/berita', 1309620134, 14),
(23, '/berita', 1309620134, 14),
(24, '/berita', 1309620134, 14),
(25, '/berita', 1309620134, 14),
(26, '/berita', 1309620134, 14),
(27, '/berita', 1309620134, 14),
(28, '/berita', 1309620134, 14),
(29, '/berita', 1309620134, 14),
(30, '/berita', 1309620134, 14),
(31, '/berita', 1309620134, 14),
(32, '/berita', 1309620134, 14),
(33, '/berita', 1309620134, 14),
(34, '/daftar', 1309620134, 7),
(35, '/start', 948159175, 1),
(36, '/bantuan', 948159175, 4),
(37, '/daftar', 948159175, 7),
(38, '/daftar\nBejjo\nBejjo@gmail.com\nmr', 948159175, 7),
(39, '/daftar', 948159175, 7),
(40, '/foto', 948159175, 8),
(41, '/foto', 948159175, 8),
(42, '/daftar', 948159175, 7),
(43, '/foto', 948159175, 8),
(44, '/status', 1309620134, 15),
(45, '/status', 1309620134, 15),
(46, '/status', 1309620134, 15),
(47, '/bantuan', 1309620134, 4),
(48, '/tolong', 1309620134, 3),
(49, '/bantuan', 1309620134, 4),
(50, '/daftar', 1309620134, 7),
(51, '/foto', 948159175, 8),
(52, '/foto', 948159175, 8),
(53, '/daftar\nBejjo eqq\nbejjoeqq@gmail.com\nmr', 948159175, 7);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pkkp_key`
--

CREATE TABLE `pkkp_key` (
  `key_id` int(11) NOT NULL,
  `key_word` varchar(50) NOT NULL,
  `key_count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pkkp_key`
--

INSERT INTO `pkkp_key` (`key_id`, `key_word`, `key_count`) VALUES
(1, '/start', 4),
(2, '/hey', 1),
(3, '/tolong', 2),
(4, '/bantuan', 4),
(5, '/saran', 2),
(6, '/info', 1),
(7, '/daftar', 8),
(8, '/foto', 7),
(9, '/hasil', 1),
(10, '/materi', 1),
(11, '/pembekalan', 1),
(12, '/syarat', 1),
(13, 'etc', 3),
(14, '/berita', 14),
(15, '/status', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pkkp_level`
--

CREATE TABLE `pkkp_level` (
  `admin_level` int(11) NOT NULL,
  `level_text` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pkkp_level`
--

INSERT INTO `pkkp_level` (`admin_level`, `level_text`) VALUES
(1, 'owner'),
(2, 'admin'),
(3, 'content');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pkkp_admin`
--
ALTER TABLE `pkkp_admin`
  ADD PRIMARY KEY (`admin_id`),
  ADD KEY `admin_level` (`admin_level`);

--
-- Indexes for table `pkkp_berita`
--
ALTER TABLE `pkkp_berita`
  ADD PRIMARY KEY (`berita_id`);

--
-- Indexes for table `pkkp_daftar`
--
ALTER TABLE `pkkp_daftar`
  ADD PRIMARY KEY (`daftar_idtele`);

--
-- Indexes for table `pkkp_history`
--
ALTER TABLE `pkkp_history`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `history_tipe` (`key_id`),
  ADD KEY `history_user` (`daftar_idtele`);

--
-- Indexes for table `pkkp_key`
--
ALTER TABLE `pkkp_key`
  ADD PRIMARY KEY (`key_id`);

--
-- Indexes for table `pkkp_level`
--
ALTER TABLE `pkkp_level`
  ADD PRIMARY KEY (`admin_level`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pkkp_admin`
--
ALTER TABLE `pkkp_admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `pkkp_berita`
--
ALTER TABLE `pkkp_berita`
  MODIFY `berita_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `pkkp_history`
--
ALTER TABLE `pkkp_history`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
--
-- AUTO_INCREMENT for table `pkkp_key`
--
ALTER TABLE `pkkp_key`
  MODIFY `key_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `pkkp_level`
--
ALTER TABLE `pkkp_level`
  MODIFY `admin_level` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `pkkp_admin`
--
ALTER TABLE `pkkp_admin`
  ADD CONSTRAINT `pkkp_admin_ibfk_1` FOREIGN KEY (`admin_level`) REFERENCES `pkkp_level` (`admin_level`);

--
-- Ketidakleluasaan untuk tabel `pkkp_history`
--
ALTER TABLE `pkkp_history`
  ADD CONSTRAINT `pkkp_history_ibfk_1` FOREIGN KEY (`key_id`) REFERENCES `pkkp_key` (`key_id`),
  ADD CONSTRAINT `pkkp_history_ibfk_2` FOREIGN KEY (`daftar_idtele`) REFERENCES `pkkp_daftar` (`daftar_idtele`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
