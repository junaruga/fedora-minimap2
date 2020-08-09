Name: minimap2
Version: 2.17
Release: 1%{?dist}
Summary: A versatile pairwise aligner for genomic and spliced nucleotide sequences

License: MIT
URL: https://lh3.github.io/minimap2/
Source0: https://github.com/lh3/%{name}/archive/v%{version}.tar.gz
# Add Makefile.simde, as Makefile.simde is not shipped on minimap2 2.17.
# https://github.com/lh3/minimap2/commit/ccb0f7b05df3a17011f0d0f4388ddb301198871b
# https://github.com/lh3/minimap2/pull/607
Source1: Makefile.simde
# A patch to build with simde.
# https://github.com/lh3/minimap2/pull/597
Patch0: minimap2-2.17-simde.patch

BuildRequires: gcc
BuildRequires: simde-devel
BuildRequires: zlib-devel

%description

Minimap2 is a versatile sequence alignment program that aligns DNA or mRNA
sequences against a large reference database. Typical use cases include: (1)
mapping PacBio or Oxford Nanopore genomic reads to the human genome; (2)
finding overlaps between long reads with error rate up to ~15%; (3)
splice-aware alignment of PacBio Iso-Seq or Nanopore cDNA or Direct RNA reads
against a reference genome; (4) aligning Illumina single- or paired-end reads;
(5) assembly-to-assembly alignment; (6) full-genome alignment between two
closely related species with divergence below ~15%.


%prep
# %%autosetup -p1
%setup -q
%patch0 -p1
cp -p "%{SOURCE1}" .


%build
%set_build_flags
# Set sse2only=1 to avoid the build error.
%make_build -f Makefile.simde sse2only=1


%install
%make_install


%files
%license LICENSE.txt
%doc FAQ.md NEWS.md README.md cookbook.md


%changelog
* Wed Aug  5 2020 Jun Aruga <jaruga@redhat.com>
- Initial package
