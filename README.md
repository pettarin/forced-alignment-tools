# forced-alignment-tools

A collection of links and notes on forced alignment tools

* Version: 1.0.9
* Date: 2018-07-10
* Author: [Alberto Pettarin](http://www.albertopettarin.it/) ([contact](http://www.albertopettarin.it/contact.html))
* License: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode)

Did I miss an aligner? Please open an issue or directly fork-commit-pullrequest.

## Definition of Forced Alignment

Given an audio file containing speech,
and the corresponding transcript,
computing a **forced alignment** is the process of
determining, for each fragment of the transcript,
the **time interval** (in the audio file)
containing the spoken text of the fragment.

A text fragment can have arbitrary granularity:

* a paragraph,
* a sentence,
* a portion of a sentence (i.e., a group of words),
* a word, or
* a phoneme (i.e., a single sound).

For example, given
[this text file](https://raw.githubusercontent.com/readbeyond/aeneas/master/aeneas/tests/res/container/job/assets/p001.xhtml)
and
[this audio file](https://raw.githubusercontent.com/readbeyond/aeneas/master/aeneas/tests/res/container/job/assets/p001.mp3),
a force aligment at verse-level can be the following:

```
1                                                     => [00:00:00.000, 00:00:02.640]
From fairest creatures we desire increase,            => [00:00:02.640, 00:00:05.880]
That thereby beauty's rose might never die,           => [00:00:05.880, 00:00:09.240]
But as the riper should by time decease,              => [00:00:09.240, 00:00:11.920]
His tender heir might bear his memory:                => [00:00:11.920, 00:00:15.280]
...
Pity the world, or else this glutton be,              => [00:00:43.640, 00:00:48.080]
To eat the world's due, by the grave and thee.        => [00:00:48.080, 00:00:53.240]
```

Typical **applications** of forced alignment include
[Audio-eBooks](https://www.readbeyond.it/audioebooks.html),
[closed captioning](https://en.wikipedia.org/wiki/Closed_captioning),
and automating the creation of training data
for automated speech recognition systems.


## Programs and Libraries

The following matrix contains **open source** programs and libraries
for computing forced alignments
that have been actually **proven to install and run**
(albeit the installation procedure for some of them is pretty complex).

All tools, except **aeneas**, are based on speech recognition algorithms;
all tools, except **aeneas** and **gentle**,
are maintained by research groups or individuals in academia.

Most tools are based on the [HTK](http://htk.eng.cam.ac.uk/),
which is not free for commercial purposes,
although a commercial license can be purchased
from the University of Cambridge.

You can also download the [raw data file in JSON format](data.json).

| Name | Algorithm | Supported Language(s) | Interface | Code Language(s) | License | Documentation | Mailing List/Forum | Active | Notes |
| ---- | --------- | --------------------- | --------- | ---------------- | ------- | ------------- | ------------------ | ------ | ----- |
| [aeneas](https://www.readbeyond.it/aeneas/) | DTW | 30+ | CLI, LIB, Web | Python, C | AGPL | Y | Y | Y | Not based on ASR |
| [CMU Sphinx](http://cmusphinx.sourceforge.net/) | HMM (own), RNN | 11 | CLI, LIB | C, Java, Python | MIT-like | Y | Y | Y |  |
| [DARLA](http://darla.dartmouth.edu/cave) | HMM (HTK) | English | Web | ? | ? | Y | N | N? | Based on Prosodylab-Aligner or YouTube ASR |
| [FAVE-align](https://github.com/JoFrhwld/FAVE/) | HMM (HTK) | English | CLI, (Web) | Python | GPL | Y | Y | Y | acustic models from P2FA; GitHub code updated more frequently than Web |
| [Gentle](https://lowerquality.com/gentle/) | HMM (Kaldi) | English | CLI, Web | Python | MIT | N | N | Y | Based on Kaldi |
| [Julius](http://julius.osdn.jp/en_index.php) | HMM (own) | English, Japanese | CLI, LIB | C | MIT-like | Y | Y | N? |  |
| [Kaldi](http://kaldi-asr.org/) | HMM (own), DNN, RNN | English | CLI, LIB | C++ | Apache | Y | Y | Y | CUDA support |
| [kaldi-dnn-ali-gop](https://github.com/tbright17/kaldi-dnn-ali-gop) | HMM(Kaldi), DNN(Kaldi nnet3) | English | CLI, LIB | Shell Script, C++, Python | GPL | N | N | Y | Work with other languages given kaldi acoustic models |
| [LaBB-CAT](http://labbcat.sourceforge.net/) | HMM (HTK) | English | Web | Java | GPL | Y | Y | Y |  |
| [MAUS](https://www.phonetik.uni-muenchen.de/forschung/Verbmobil/VM14.7eng.html) | HMM (HTK) | 21 | CLI, Web | C | All rights reserved | README | Y | Y |  |
| [Montreal Forced Aligner](https://montrealcorpustools.github.io/Montreal-Forced-Aligner/) | HMM (Kaldi) | English | CLI | Python | MIT | Y | N | Y | Can train other languages |
| [Penn Forced Aligner (P2FA)](https://www.ling.upenn.edu/phonetics/old_website_2015/p2fa/) | HMM (HTK) | English | CLI, Web | Python | ? | README, Tutorial | N | N? |  |
| [Prosodylab-Aligner](http://prosodylab.org/tools/aligner/) | HMM (HTK) | English | CLI | Python | MIT | README, Tutorial | N | Y | Can train other languages |
| [SailAlign](https://github.com/nassosoassos/sail_align) | HMM (HTK) | English, Greek, Spanish | CLI | Perl | GPL | README | N | N? |  |
| [SPPAS](http://www.sppas.org/index.html) | HMM (Julius) | 12+ | CLI, GUI | Python | GPL | Y | Y | Y | Can train other language, several plugins |

* AGPL: [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.html)
* Apache: [Apache License](http://www.apache.org/licenses/LICENSE-2.0)
* CLI: command line interface
* DNN: [Deep Neural Network](https://en.wikipedia.org/wiki/Deep_learning)
* DTW: [Dynamic Time Warping](https://en.wikipedia.org/wiki/Dynamic_time_warping)
* GPL: [GNU General Public License](https://www.gnu.org/licenses/gpl.html)
* GUI: graphical interface
* HMM: [Hidden Markov Model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
* LIB: library callable by third party software
* MFCC: [Mel-frequency Cepstral Coefficients](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
* MIT: [MIT License](https://opensource.org/licenses/MIT)
* RNN: [Recurrent Neural Network](https://en.wikipedia.org/wiki/Recurrent_neural_network)
* Web: Web-based graphical interface, local and/or remote

## Additional Pointers

* [AZP2FA](https://github.com/myedibleenso/AZP2FA) (fork of P2FA)
* [Automated Audio Segmentation Using Forced Alignment](http://www.voxforge.org/home/dev/autoaudioseg)
* [Automatic and Accurate Captioning](http://www.nmsl.cs.ucsb.edu/proj/autocap/) (based on CMU Sphinx)
* [Berkeley Phonetics Machine](http://linguistics.berkeley.edu/plab/guestwiki/index.php?title=Berkeley_Phonetics_Machine)
* [Building Acoustic Models using Kaldi Voxforge recipe to obtain word level transcripts for long video files](http://forcedalignment.blogspot.it/2015/06/building-acoustic-models-using-kaldi.html)
* [DARLA](http://darla.dartmouth.edu/cave)
* [EasyAlign: phonetic alignment with Praat](http://latlcui.unige.ch/phonetique/easyalign.php)
* [FAVE-align](http://fave.ling.upenn.edu/) (the Web interface for the Penn Forced Aligner)
* [FAVE-align](https://github.com/JoFrhwld/FAVE/) (source code)
* [Forced Alignment Overview (ISIP)](https://www.isip.piconepress.com/projects/speech/software/tutorials/production/fundamentals/v1.0/section_04/s04_04_p01.html)
* [Forced Alignment and Speech Recognition Systems (Oxford)](http://www.phon.ox.ac.uk/jcoleman/BAAP_ASR.pdf)
* [Forced Alignment of Spoken Audio](https://www.clarin.eu/sites/default/files/Joe_Fruehwald_Oxford_2016.pdf)
* [Forced Alignment with InproTK (and Sphinx)](http://www.dsg-bielefeld.de/dsg_wp/forced-alignment-with-inprotk-and-sphinx/)
* [Gentle](https://lowerquality.com/gentle/) (based on Kaldi)
* [HTKBook](http://htk.eng.cam.ac.uk/docs/docs.shtml) (has a chapter on computing forced alignments with HTK, requires registration)
* [InproTK](https://bitbucket.org/inpro/inprotk)
* [Introduction to Speech Analysis with FAVE](https://jofrhwld.github.io/workshop/fave2015.html)
* [Julius](http://julius.osdn.jp/en_index.php)
* [Kaldi Forced Alignment](http://pages.jh.edu/~echodro1/tutorial/kaldi/kaldi-forcedalignment.html)
* [Kaldi](http://kaldi-asr.org/)
* [Korean Phonetic Aligner](http://korean.utsc.utoronto.ca/kpa/) (Web only, Korean only)
* [LaBB-CAT](http://labbcat.sourceforge.net/)
* [Long Audio Aligner Landed in Trunk (Sphinx)](http://cmusphinx.sourceforge.net/2014/07/long-audio-aligner-landed-in-trunk/)
* [MAUS](https://www.phonetik.uni-muenchen.de/forschung/Verbmobil/VM14.7eng.html)
* [Montreal Forced Aligner](https://montrealcorpustools.github.io/Montreal-Forced-Aligner/)
* [Penn Forced Aligner](http://pages.jh.edu/~echodro1/tutorial/pfa/pfa-intro.html)
* [Penn Forced Aligner](https://www.ling.upenn.edu/phonetics/old_website_2015/p2fa/)
* [Praatalign: an interactive Praat plug-in for performing phonetic forced alignment](https://github.com/dopefishh/praatalign)
* [ProsodyLab-Aligner](http://prosodylab.org/tools/aligner/)
* [Robust Automatic Transcription of Speech (RATS)](http://opencatalog.darpa.mil/RATS.html)
* [SPPAS Automatic Annotation of Speech](http://www.sppas.org/index.html) (based on Julius)
* [Simple English Forced Alignment (UPenn LING521)](http://www.ling.upenn.edu/courses/ling521/NewAligner1a.html)
* [VoxForge](http://www.voxforge.org/)
* [WebMAUS](https://clarin.phonetik.uni-muenchen.de/BASWebServices/index.html#/services/WebMAUSBasic) (the Web interface for MAUS)
* [What is forced alignment? (ICSI)](http://www1.icsi.berkeley.edu/Speech/faq/forcedalign.html)
* [What is forced alignment? (VoxForge)](http://www.voxforge.org/home/docs/faq/faq/what-is-forced-alignment))
* [aeneas](https://www.readbeyond.it/aeneas/)
* [speech.zone](http://www.speech.zone/)



