from core.models import BaseModel

from django.db import models


class Lead(BaseModel):
    class LeadStatusChoices(models.TextChoices):
        # INÍCIO DO PROCESSO
        NEW = 'new', 'Novo'  # Acabou de entrar
        PENDING = 'pending', 'Pendente' # Atribuído, aguardando 1º contato ou tentativa falha
        # PROSPECÇÃO
        ON_HOLD_SCHEDULED = 'on_hold_scheduled', 'Em Espera (Agendado)'
        ATTEMPTING_CONTACT = 'attempting_contact', 'Tentativa de Contato' # Vendedor tentando ativamente
        IN_CONTACT = 'in_contact', 'Em Contato' # Conectado, conversando
        # QUALIFICAÇÃO/AVANÇO
        QUALIFIED = 'qualified', 'Qualificado' # Perfil validado, interesse confirmado
        DEVELOPMENT = 'development', 'Desenvolvimento / Prova' # Onde entra a 'amostra'
        # FECHAMENTO
        PROPOSAL_SENT = 'proposal_sent', 'Proposta Enviada' # Fase final de negociação
        # RESULTADO
        CLOSED = 'closed', 'Fechado (Cliente)'
        UNQUALIFIED = 'unqualified', 'Desqualificado'

    company_name = models.CharField('Nome da empresa', max_length=255)
    contact_name = models.CharField(
        'Nome do contato',
        max_length=255,
        blank=True,
        null=True
    )
    niche = models.CharField('Nicho', max_length=30)
    phone_number = models.CharField(
        'Contato',
        max_length=20,
        blank=True,
        null=True
    )
    has_whatsapp = models.BooleanField('Tem Whatsapp?', default=True)
    website_link = models.CharField(
        'Link do site',
        max_length=255,
        blank=True,
        null=True
    )
    lead_origin = models.CharField(
        'Origem do lead',
        max_length=255,
        blank=True,
        null=True
    )
    contact_status = models.CharField(
        'Status',
        max_length=50,
        choices=LeadStatusChoices.choices,
        default=LeadStatusChoices.NEW
    )
    observations = models.TextField('Observações', blank=True, null=True)
    return_date = models.DateTimeField(
        'Data/Hora de Retorno',
        blank=True,
        null=True,
    )
    

    class Meta:
        ordering = ('company_name',)
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
    
    def __str__(self):
        return self.company_name
