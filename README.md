# encryptedMessageRiddle
<p>
This is a project I wrote for Advanced Computational Linguistics class.
It uses <a href="https://en.wikipedia.org/wiki/Simulated_annealing">simulated annealing</a> to decrypt a message.
<br> Here are parts of the instructions given for this project:
<br><em>"A North Korean spy, imprisoned in a local prison in Los Angeles, was caught sending an encrypted
<br>message written using an encryption system known as the Substitution Cipher. That is, each alphabetic
<br>letter is replaced with another letter. Scientists from a local university were the ones to intercept the
<br>message (provided on Piazza as problemset 06 encrypted input.txt), and they ask for your help:
<br>find the encryption key (i.e. letter permutation) used by the spy! Decrypt the message! Save the world!"</em>
</p>

<h2>Technical Details</h2>
<p>
  it takes about 4-5 minutes to the program to exacute.
  <br>The program prints the decrypted message, and the dictionary that is needed in order to decrypt it.
</p>
<h3>Files</h3>
<ul>
  <li><em>problemset_06_encrypted_input.txt</em> is the encrypted text</li>
  <li><em>language_model.py</em> containing the functionality needed in order to read a corpus from an online resource and build an bigram language model</li>
  <li><em>permutation.py</em> representing a letter permutation = the dictionary</li>
  <li><em>simulated_annealing.py</em> containing an implementation of the simulated annealing algorithm for finding the optimal hypothesis in a large conjecture space</li>
  <li><em>main.py</em> main function.</li>
</ul>
