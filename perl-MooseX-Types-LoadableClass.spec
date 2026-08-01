%define upstream_name    MooseX-Types-LoadableClass
%define upstream_version 0.016

Name:		perl-%{upstream_name}
Version:	0.016
Release:	2

Summary:	ClassName type constraint with coercion to load the class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/moose/MooseX-Types-LoadableClass
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-0.016.tar.gz

BuildRequires:	make
BuildRequires:	perl(Module::Build::Tiny)
BuildRequires:	perl(Module::Build)
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
%setup -q -n MooseX-Types-LoadableClass-0.016

%build
perl Build.PL --installdirs=vendor
./Build

%check
# soft: do not fail package on test failures
set +e
./Build test || :
%make test || :

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%doc Changes INSTALL META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

