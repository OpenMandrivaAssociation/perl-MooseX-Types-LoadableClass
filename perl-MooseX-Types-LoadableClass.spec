%define upstream_name    MooseX-Types-LoadableClass
%define upstream_version 0.012

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	ClassName type constraint with coercion to load the class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-Types-LoadableClass-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Test::Fatal)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
    use Moose::Util::TypeConstraints;

    my $tc = subtype as ClassName;
    coerce $tc, from Str, via { Class::MOP::load_class($_); $_ };

I've written those three lines of code quite a lot of times, in quite a lot
of places.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 657800
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 602091
- import perl-MooseX-Types-LoadableClass


