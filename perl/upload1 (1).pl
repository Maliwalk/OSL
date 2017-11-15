#!Perl
use strict; 
use CGI; 
use CGI::Carp qw ( fatalsToBrowser ); 
use File::Basename; 
$CGI::POST_MAX = 1024 * 5000; 
my $safe_filename_characters = "a-zA-Z0-9_.-"; 
my $upload_dir = "C:\\wamp\\www\\cgi-bin\\upload"; 
my @files = glob "$upload_dir/*";
my $query = new CGI; 
my $filename = $query->param("photo"); 
my $email_address = $query->param("email_address"); 
if ( !$filename ) { 
	print $query->header ( ); 
	print "There was a problem uploading your photo (try a smaller file)."; 
	exit; 
} 

if (file_exists($target_file)) {
    print "Sorry, file already exists.";
    $uploadOk = 0;
}
if ($_FILES["file"]["size"] > 50000000) {
    print "Sorry, your file is too large.";
    $uploadOk = 0;
}
if($imageFileType != "jpg" && $imageFileType != "txt" && $imageFileType !="pdf" ){
    print "Sorry, only JPG and TXT files are allowed.";
    $uploadOk = 0;
}
if ($uploadOk == 0) {
    print "Sorry, your file was not uploaded.";
} else {
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        print "The file ". basename( $_FILES["file"]["name"]). " has been uploaded as ". $newname.".".$imageFileType;
    } else {
        print "Sorry, there was an error uploading your file.";
    }
}


my ( $name, $path, $extension ) = fileparse ( $filename, '..*' ); 
$filename = $name . $extension; $filename =~ tr/ /_/; 
$filename =~ s/[^$safe_filename_characters]//g; 
if ( $filename =~ /^([$safe_filename_characters]+)$/ ) { 
	$filename = $1; 
} else { 
	die "Filename contains invalid characters"; 
} 


my $upload_filehandle = $query->upload("photo"); 
open ( UPLOADFILE, ">$upload_dir\\$filename" ) or die "$!"; 
binmode UPLOADFILE; 
while ( <$upload_filehandle> ) { 
	print UPLOADFILE; 
} 
close UPLOADFILE; 
print $query->header( ); 
print <<END_HTML; 

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">

        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>Thanks!</title>
            <style type="text/css">
                img {
                    border: none;
                }
            </style>
        </head>

        <body>
            <p>Thanks for uploading!</p>
            <p>Hi $email_address</p>
            <p>Check out your folder to see all your files :)</p>
        </body>

        </html>
END_HTML