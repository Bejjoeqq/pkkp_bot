<?php include 'header.php'; ?>
<?php
$limit = 10;
if(isset($_GET['p']))
{
    $noPage = $_GET['p'];
}
else $noPage = 1;

$offset = ($noPage - 1) * $limit;

$sql = "SELECT daftar_nama, history_chat, key_word, history_id FROM pkkp_history INNER JOIN pkkp_daftar USING(daftar_idtele) INNER JOIN pkkp_key USING(key_id) ORDER BY history_id DESC LIMIT ".$offset.",". $limit;
$qry = $mysqli->query($sql) or die ("Error retrieving data: ".$mysqli->error);

$sql_rec = "SELECT history_id FROM pkkp_history";

$total_rec = $mysqli->query($sql_rec) or die ("Error retrieving number:".$mysqli->error);

$total_rec_num = $total_rec->num_rows;

$total_page = ceil($total_rec_num/$limit);

?>
<div class="container-fluid body">
	<div class="row">
		<div class="col-lg-2 sidebar">
			<?php include 'sidebar.php'; ?>
		</div>
		<div class="col-lg-10 main-content">
			<div class="panel panel-default">
				<div class="panel-body">
					<div class="row">
						<div class="col-md-12">
							<h2 class="page-header"><i class="fa fa-folder-o"></i> History</h2>
						</div>
					</div>
					<div class="row">
						<div class="col-md-12">
							<table class="table table-hover">
								<thead>
									<tr>
										<th width="30%">Nama</th>
										<th width="50%">History</th>
										<th width="10%">Tipe</th>
										<th width="10%">Last Chat</th>
									</tr>
								</thead>
								<tbody>
								<?php if ($total_rec_num == 0) { ?>
									<tr>
										<td colspan="5" align="center">Belum ada data</td>
									</tr>
								<?php } else { ?>
									<?php while ($pesan = $qry->fetch_assoc()) { ?>
									<tr>
										<td><?php echo $pesan['daftar_nama']; ?></td>
										<td><textarea cols="90" disabled=""><?php echo $pesan['history_chat']; ?></textarea></td>
										<td><?php echo $pesan['key_word']; ?></td>
										<td><?php echo $pesan['history_id']; ?></td>
									</tr>
									<?php } ?>
								<?php } ?>
								</tbody>
							</table>
						</div>
						<div class="col-md-12">
							<ul class="pagination">
							<?php if ($noPage > 1) { ?>

								<li>
									<a href="<?php echo "history.php?p=".($noPage-1);?>">
										<i class="glyphicon glyphicon-chevron-left"></i>
									</a>
								</li>

							<?php } ?>

							<?php for ($page=1; $page <= $total_page ; $page++) { ?>
								<?php if ((($page >= $noPage - 3) && ($page <= $noPage + 3)) || ($page == 1) || ($page == $total_page)) { ?>
									<?php
										$showPage = $page;
										if ($page==$total_page && $noPage <= $total_page-5) echo "<li class='active'><a>...</a></li>";
            							if ($page == $noPage) echo "<li class='active'><a href='#'>".$page."</a></li> ";
            							else echo " <li><a href='".$_SERVER['PHP_SELF']."?p=".$page."'>".$page."</a></li> ";
            							if ($page == 1 && $noPage >=6) echo "<li class='active'><a>...</a></li>";
									?>
								<?php } ?>
							<?php } ?>

							<?php if ($noPage < $total_page) { ?>
								<li>
									<a href="<?php echo "history.php?p=".($noPage+1); ?>">
										<i class="glyphicon glyphicon-chevron-right"></i>
									</a>
								</li>
							<?php } ?>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<?php include 'footer.php'; ?>