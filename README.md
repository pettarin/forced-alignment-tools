# forced-alignment-tools

A collection of links and notes on forced alignment tools 

* Version: 1.0.0
* Date: 2016-08-01
* Author: [Alberto Pettarin](http://www.albertopettarin.it/) ([contact](http://www.albertopettarin.it/contact.html))
* License: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode)

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
But thou contracted to thine own bright eyes,         => [00:00:15.280, 00:00:18.800]
Feed'st thy light's flame with self-substantial fuel, => [00:00:18.800, 00:00:22.760]
Making a famine where abundance lies,                 => [00:00:22.760, 00:00:25.680]
Thy self thy foe, to thy sweet self too cruel:        => [00:00:25.680, 00:00:31.240]
Thou that art now the world's fresh ornament,         => [00:00:31.240, 00:00:34.400]
And only herald to the gaudy spring,                  => [00:00:34.400, 00:00:36.920]
Within thine own bud buriest thy content,             => [00:00:36.920, 00:00:40.640]
And tender churl mak'st waste in niggarding:          => [00:00:40.640, 00:00:43.640]
Pity the world, or else this glutton be,              => [00:00:43.640, 00:00:48.080]
To eat the world's due, by the grave and thee.        => [00:00:48.080, 00:00:53.240]
```

Typical **applications** of forced alignment include
[Audio-eBooks](https://www.readbeyond.it/audioebooks.html) and
[closed captioning](https://en.wikipedia.org/wiki/Closed_captioning).


## Programs and Libraries

The following matrix contains **open source** programs and libraries
for computing forced alignments
that have been actually **proven to install and run**,
(albeit the installation procedure for some of them is pretty complex).

All tools, except **aeneas**, are based on speech recognition algorithms;
all tools, except **aeneas** and **gentle**,
are maintained by research groups or individuals in academia.

Most tools are based on the [HTK](http://htk.eng.cam.ac.uk/),
which is not free for commercial purposes
(although a commercial license can be purchased).

Name | Algorithm | Supported Language(s) | Interface | Code Language | License | Documentation | Mailing List/Forum | Active | Notes
-----|-----------|-----------------------|-----------|---------------|---------|---------------|--------------------|--------|------
[aeneas](https://www.readbeyond.it/aeneas/) | DTW | 30+ | CLI + LIB + Web | Python/C | AGPL | Y | Y | Y | Not based on speech recognition
[CMU Sphinx](http://cmusphinx.sourceforge.net/) | HMM (own) / RNN | 11 | CLI + LIB | C/Java/Python | MIT-like | Y | Y | Y | 
[Gentle](https://lowerquality.com/gentle/) | HMM (Kaldi) | English | CLI + Web | Python | MIT | N | N | Y | Based on Kaldi
[Julius](http://julius.osdn.jp/en_index.php) | HMM (own) | English, Japanese | CLI + LIB | C | MIT-like | Y | Y | N? |
[Kaldi](http://kaldi-asr.org/) | HMM (own) / DNN / RNN | English | CLI + LIB | C++ | Apache | Y | Y | Y | CUDA support
[MAUS](https://www.phonetik.uni-muenchen.de/forschung/Verbmobil/VM14.7eng.html) | HMM (HTK) | 10 | CLI + Web | C | All rights reserved | README | N | Y |
[Penn Forced Aligner](https://www.ling.upenn.edu/phonetics/old_website_2015/p2fa/) | HMM (HTK) | English | CLI + Web | Python | ??? | README, Tutorial | N | N? | 
[Prosodylab-Aligner](http://prosodylab.org/tools/aligner/) | HMM (HTK) | English | CLI | Python | ??? | README, Tutorial | N | Y | Other languages are trainable
[SailAlign](https://github.com/nassosoassos/sail_align) | HMM (HTK) | English, Greek, Spanish | CLI | Perl | GPL | README | N | N? |

Acronyms:

* DNN: [Deep Neural Network](https://en.wikipedia.org/wiki/Deep_learning)
* DTW: [Dynamic Time Warping](https://en.wikipedia.org/wiki/Dynamic_time_warping)
* MFCC: [Mel-frequency Cepstral Coefficients](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
* HMM: [Hidden Markov Model](https://en.wikipedia.org/wiki/Hidden_Markov_model)
* RNN: [Recurrent Neural Network](https://en.wikipedia.org/wiki/Recurrent_neural_network)


## Additional Pointers

* [aeneas](https://www.readbeyond.it/aeneas/)
* [Automated Audio Segmentation Using Forced Alignment](http://www.voxforge.org/home/dev/autoaudioseg)
* [Automatic and Accurate Captioning](http://www.nmsl.cs.ucsb.edu/proj/autocap/), based on CMU Sphinx
* [Building Acoustic Models using Kaldi Voxforge recipe to obtain word level transcripts for long video files](http://forcedalignment.blogspot.it/2015/06/building-acoustic-models-using-kaldi.html)
* [EasyAlign: phonetic alignment with Praat](http://latlcui.unige.ch/phonetique/easyalign.php)
* [FAVE-align](http://fave.ling.upenn.edu/), the Web interface for the Penn Forced Aligner
* [Forced Alignment and Speech Recognition Systems (Oxford)](http://www.phon.ox.ac.uk/jcoleman/BAAP_ASR.pdf)
* [Forced Alignment of Spoken Audio](https://www.clarin.eu/sites/default/files/Joe_Fruehwald_Oxford_2016.pdf)
* [Forced Alignment Overview (ISIP)](https://www.isip.piconepress.com/projects/speech/software/tutorials/production/fundamentals/v1.0/section_04/s04_04_p01.html)
* [Forced Alignment with InproTK (and Sphinx)](http://www.dsg-bielefeld.de/dsg_wp/forced-alignment-with-inprotk-and-sphinx/)
* [Gentle](https://lowerquality.com/gentle/), based on Kaldi
* [HTKBook](http://htk.eng.cam.ac.uk/docs/docs.shtml) has a chapter on computing forced alignments (with HTK), requires registration
* [InproTK](https://bitbucket.org/inpro/inprotk)
* [Introduction to Speech Analysis with FAVE](https://jofrhwld.github.io/workshop/fave2015.html)
* [Julius](http://julius.osdn.jp/en_index.php)
* [Kaldi](http://kaldi-asr.org/)
* [Kaldi Forced Alignment](http://pages.jh.edu/~echodro1/tutorial/kaldi/kaldi-forcedalignment.html)
* [Korean Phonetic Aligner](http://korean.utsc.utoronto.ca/kpa/), Web only, Korean only
* [Long Audio Aligner Landed in Trunk (Sphinx)](http://cmusphinx.sourceforge.net/2014/07/long-audio-aligner-landed-in-trunk/)
* [MAUS](https://www.phonetik.uni-muenchen.de/forschung/Verbmobil/VM14.7eng.html)
* [speech.zone](http://www.speech.zone/)
* [SPPAS Automatic Annotation of Speech](http://www.sppas.org/index.html), based on Julius
* [Penn Forced Aligner](https://www.ling.upenn.edu/phonetics/old_website_2015/p2fa/)
* [Penn Forced Aligner](http://pages.jh.edu/~echodro1/tutorial/pfa/pfa-intro.html)
* [Praatalign: an interactive Praat plug-in for performing phonetic forced alignment](https://github.com/dopefishh/praatalign)
* [ProsodyLab-Aligner](http://prosodylab.org/tools/aligner/)
* [VoxForge](http://www.voxforge.org/)
* [WebMAUS](https://clarin.phonetik.uni-muenchen.de/BASWebServices/index.html#/services/WebMAUSBasic), the Web interface for MAUS
* [What is forced alignment? (ICSI)](http://www1.icsi.berkeley.edu/Speech/faq/forcedalign.html)
* [What is forced alignment? (VoxForge)](http://www.voxforge.org/home/docs/faq/faq/what-is-forced-alignment)



