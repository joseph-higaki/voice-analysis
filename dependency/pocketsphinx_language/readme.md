CMY Sphinx

Acoustic and Language Model

https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/

Download the three file
THey will be the sphinx_language_parameters for 

```python 

sphinx_language_parameter = {\
    "es": (\
    "/workspaces/voice-analysis/dependency/pocketsphinx_language/cmusphinx-es-5.2/cmusphinx-es-5.2/model_parameters/voxforge_es_sphinx.cd_ptm_4000",\
    "/workspaces/voice-analysis/dependency/pocketsphinx_language/es-20k.lm.gz",\
    "/workspaces/voice-analysis/dependency/pocketsphinx_language/es.dict"
    ),
    "en": "en-US"
}

text_by_sphinx = recognizer.recognize_sphinx(audio_data, sphinx_language_parameter[audio_filename_language])
```

They will be set as follows at `speech_recognition__init__.py`
```python
        # create decoder object
        config = pocketsphinx.Decoder.default_config()
        config.set_string("-hmm", acoustic_parameters_directory)  # set the path of the hidden Markov model (HMM) parameter files
        config.set_string("-lm", language_model_file)
        config.set_string("-dict", phoneme_dictionary_file)
```

## [cmusphinx-es-5.2.tar.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/cmusphinx-es-5.2.tar.gz/download)
Unzip 


## [es.dict](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/es.dict/download)

## [es-20k.lm.gz](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/es-20k.lm.gz/download)
