# Code to brute force finding good handles given the original set of strands

from nupack import *
import itertools
import numpy

my_model = Model(material='dna04-nupack3',
                 ensemble='some-nupack3',
                 celsius=25,
                 sodium=0.05,
                 magnesium=0.01)

bases = ['A', 'C', 'T', 'G']

self_dG_thresh = -0.8
bind_dG_min = -10.5
bind_dG_max = -8.5
nonbind_dG_thresh = -7

ImA = Strand('AGGCGTCATCACATA', name='ImA')
ImB = Strand('ATGCGGAAAAGACTA', name='ImB')
ImC = Strand('AGTCTTATACAACCA', name='ImC')
ims = [ImA, ImB, ImC]

for seq in itertools.product(bases, repeat=12):

    Handle = Strand(''.join(['TC'] + list(seq) + ['T']), name='Handle')

    dG_self = pfunc(strands=[Handle], model=my_model)[1]
    if dG_self < self_dG_thresh:
        continue

    handle = numpy.zeros(3)

    ImA_Handle = pfunc(strands=[ImA, Handle], model=my_model)[1]
    if ImA_Handle < bind_dG_min or (ImA_Handle > bind_dG_max
                                    and ImA_Handle < nonbind_dG_thresh):
        continue
    elif ImA_Handle < bind_dG_max:
        handle += numpy.array([ImA_Handle, 0, 0])

    ImB_Handle = pfunc(strands=[ImB, Handle], model=my_model)[1]
    if ImB_Handle < bind_dG_min or (ImB_Handle > bind_dG_max
                                    and ImB_Handle < nonbind_dG_thresh):
        continue
    elif ImB_Handle < bind_dG_max:
        handle += numpy.array([0, ImB_Handle, 0])

    ImC_Handle = pfunc(strands=[ImC, Handle], model=my_model)[1]
    if ImC_Handle < bind_dG_min or (ImC_Handle > bind_dG_max
                                    and ImC_Handle < nonbind_dG_thresh):
        continue
    elif ImC_Handle < bind_dG_max:
        handle += numpy.array([0, 0, ImC_Handle])

    if numpy.sum(handle) != 0:
        for i, im in enumerate(ims):
            if handle[i] == 0:
                handle[i] = pfunc(strands=[im, Handle], model=my_model)[1]
        with open('handles_C.txt', 'a') as f:
            f.write(''.join(['TC'] + list(seq) + ['T']) + ' ' + str(handle) +
                    '\n')

with open('handles_C.txt', 'a') as f:
    f.write('done')
