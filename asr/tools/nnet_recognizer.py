#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pathlib import Path
from kaldi.asr import NnetLatticeFasterRecognizer, LatticeLmRescorer
from kaldi.decoder import LatticeFasterDecoderOptions
from kaldi.fstext import SymbolTable, shortestpath, indices_to_symbols
from kaldi.fstext.utils import get_linear_symbol_sequence
from kaldi.nnet3 import NnetSimpleComputationOptions
from kaldi.util.table import SequentialMatrixReader

def recognizer(final, hclg, words):
# Construct recognizer
    decoder_opts = LatticeFasterDecoderOptions()
    decoder_opts.beam = 13
    decoder_opts.max_active = 7000
    decodable_opts = NnetSimpleComputationOptions()
    decodable_opts.acoustic_scale = 1.0
    decodable_opts.frame_subsampling_factor = 3
    decodable_opts.frames_per_chunk = 150
    try:
        asr = NnetLatticeFasterRecognizer.from_files(final,hclg,words, decoder_opts=decoder_opts, decodable_opts=decodable_opts)
        return asr
    except Exception as e: print("RECOGNIZER ERROR: "+e)

# Construct symbol table
  #  try:
   #     symbols = SymbolTable.read_text(words)
    #    phi_label = symbols.find_index("#0")
    #except Exception as e: print(e)


# Define feature pipelines as Kaldi rspecifiers
def recognition(asr):
    try:
        feats_rspec = "ark:compute-mfcc-feats --config=conf/mfcc_hires.conf scp:temp/wav.scp ark:- |"
    except Exception as e: print("FEATS ERROR: " + e)

# Decode wav files
    try:
        with SequentialMatrixReader(feats_rspec) as f:
             for (fkey, feats) in SequentialMatrixReader(feats_rspec):
                 out = asr.decode((feats))
                 return out['text']
    except Exception as e:
        print("DECODE ERROR: "+e)
