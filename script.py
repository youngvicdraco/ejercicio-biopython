from Bio import SeqID
from Bio.Seqfeature import featuresLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename):
  record = SeqID.read(filemame, "genbank")print("Name: ", record.name)
