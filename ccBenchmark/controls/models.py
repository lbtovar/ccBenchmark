from django.db import models


class Benchmark(models.Model):
    TECHNOLOGIES = (
        ('db', 'Database'),
        ('web', 'Web Server'),
        ('app', 'Application Server'),
        ('dev', 'Application Security & Development'),
        ('svc', 'Application Services'),
        ('cloud', 'Cloud Services'),
        ('browser', 'Browser'),
        ('desk', 'Desktop'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
    effective_date = models.DateField('effective')
    technology = models.CharField(max_length=10, choices=TECHNOLOGIES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Section(models.Model):
    benchmark = models.ForeignKey(Benchmark, on_delete=models.PROTECT)
    sect_id = models.IntegerField()
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.sect_id) + " " + self.title

    class Meta:
        ordering = ('sect_id',)


class Control(models.Model):
    PROFILES = (
        ('1', 'Level 1'),
        ('2', 'Level 2'),
    )
    benchmark = models.ForeignKey(Benchmark, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    doc_id = models.CharField(max_length=5, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    scored = models.BooleanField(default=False)
    profile = models.CharField(max_length=10, choices=PROFILES)
    cci_number = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    rationale = models.TextField(null=True, blank=True)
    audit = models.TextField(null=True, blank=True)
    commands = models.TextField(null=True, blank=True)
    remediation = models.TextField(null=True, blank=True)
    impact = models.TextField(null=True, blank=True)
    default = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.doc_id + " " + self.title

    class Meta:
        ordering = ('doc_id',)
        unique_together = ['benchmark', 'doc_id']


class Project(models.Model):
    name = models.CharField(max_length=50)
    poc = models.CharField(max_length=50)
    due_date = models.DateField('analysis due')
    controls = models.ManyToManyField(Control, through='Remediation')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Remediation(models.Model):
    STATUS = (
        ('NR', 'Not Reviewed'),
        ('Y', 'Yes'),
        ('N', 'No'),
        ('NA', 'Not Applicable'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="remediation_project")
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name="remediation_control")
    status = models.CharField(max_length=20, choices=STATUS, null=False, blank=False)
    action = models.TextField(null=True, blank=True)
    who = models.CharField(max_length=50, null=True, blank=True)
    remediation_date = models.DateField('remediation date', null=True, blank=True)

    def __str__(self):
        return self.control.doc_id + " " + self.control.title + "  -  " + self.status

    class Meta:
        ordering = ('control_id',)
        unique_together = ['project', 'control']

