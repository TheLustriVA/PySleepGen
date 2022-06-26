from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('C:\\Code\\PySleepGen\\output_rnn\\rnn_sleep_script.csv', num_epochs=1)
textgen.generate()