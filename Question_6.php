<?php

$xml_content = file_get_contents("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775");

//echo $xml_content;

//$xml = simplexml_load_string($xml_content);

$xml = new SimpleXMLElement($xml_content);

//print_r($xml->Cube);

$fp = fopen('usd_currency_rates.csv', 'w');
fputcsv($fp, ['Currency Code', 'Rate']);

foreach ($xml->Cube->Cube->Cube as $cube) {
    
    //print_r($cube);
    //$linha = $cube['currency'] . ",". $cube['rate'];
    $linha = [$cube['currency'], $cube['rate']];
    //print_r($linha);
    fputcsv($fp, $linha);

}

fclose($fp);


?>
