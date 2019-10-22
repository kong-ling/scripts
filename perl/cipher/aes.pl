### example 1
use Crypt::Mode::CBC;
 
my $key = '...'; # length has to be valid key size for this cipher
my $iv = '...';  # 16 bytes
my $cbc = Crypt::Mode::CBC->new('AES');
my $ciphertext = $cbc->encrypt("secret data", $key, $iv);
 
#### example 2 (slower)
#use Crypt::CBC;
#use Crypt::Cipher::AES;
# 
#my $key = '...'; # length has to be valid key size for this cipher
#my $iv = '...';  # 16 bytes
#my $cbc = Crypt::CBC->new( -cipher=>'Cipher::AES', -key=>$key, -iv=>$iv );
#my $ciphertext = $cbc->encrypt("secret data");
