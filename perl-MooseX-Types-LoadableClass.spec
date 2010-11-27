%define upstream_name    MooseX-Types-LoadableClass
%define upstream_version 0.005

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    ClassName type constraint with coercion to load the class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
    use Moose::Util::TypeConstraints;

    my $tc = subtype as ClassName;
    coerce $tc, from Str, via { Class::MOP::load_class($_); $_ };

I've written those three lines of code quite a lot of times, in quite a lot
of places.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


