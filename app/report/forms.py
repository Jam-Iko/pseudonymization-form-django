from django import forms

PSEUDO_FUNCTIONS = {
    "cipher": "Псевдонімізуюча функція: Шифрування.",
    "auth_determined": "Псевдонімізуюча функція: Код автентифікації повідомлення. Політика: Детермінована",
    "auth_random": "Псевдонімізуюча функція: Код автентифікації повідомлення. Політика: Повністю випадкова",
    "hash_determined": "Псевдонімізуюча функція: Криптографічна хеш-функція. Політика: Детермінована",
    "hash_random": "Псевдонімізуюча функція: Криптографічна хеш-функція. Політика: Повністю випадкова",
    "randint_determined": "Псевдонімізуюча функція: Генератор випадкових чисел. Політика: Детермінована",
    "randint_random": "Псевдонімізуюча функція: Генератор випадкових чисел. Політика: Детермінована",
    "counter_determined": "Псевдонімізуюча функція: Лічильник. Політика: Детермінована",
    "counter_random": "Псевдонімізуюча функція: Лічильник. Політика: Повністю випадкова",
    "store_sensitive": "Повідомлення із рекомендацією розглянути Просунуті/Розширені техніки псевдонімізації описані ENISA [13]",
    "subject_of_pii": "Повідомлення із загальними рекомендаціями щодо захисту персональних даних та побудови комплексу дій із захисту персональних даних згідно існуючих методологій",
    "third_pt_col_pseudo": "Повідомлення із загальними рекомендаціями щодо захисту персональних даних та побудови комплексу дій із захисту персональних даних згідно існуючих методологій. Також рекомендація про обов'язкову перевірку інформаційної безпеки при виборі третьої сторони.",
    "cntrl_col_third_pt_pseudo": "Повідомлення із загальними рекомендаціями щодо захисту персональних даних та побудови комплексу дій із захисту персональних даних згідно існуючих методологій. Також рекомендація про обов'язкову перевірку інформаційної безпеки при виборі партнера/постачальника."
}
PSEUDO_VAR = {
    "cipher": [
        ('large', '', 'yes', 'no', 'yes'),
        ('medium', 'large_amount', 'yes', 'no', 'yes'),
        ('small', 'large_amount', 'yes', 'no', 'yes'),
        ('large', '', 'yes', 'no', 'no'),
        ('medium', 'large_amount', 'yes', 'no', 'no'),
        ('small', 'large_amount', 'yes', 'no', 'no'),
        ('medium', 'medium_amount', 'no', 'no', 'yes'),
        ('medium', 'medium_amount', 'no', 'no', 'no'),
    ],
    "auth_determined": [
        ('large', '', 'yes', 'yes', 'yes'),
        ('medium', 'large_amount', 'yes', 'yes', 'yes'),
        ('small', 'large_amount', 'yes', 'yes', 'yes'),
        ('large', '', 'no', 'yes', 'yes'),
        ('medium', 'large_amount', 'no', 'yes', 'yes'),
        ('small', 'large_amount', 'no', 'yes', 'yes'),
        ('medium', 'medium_amount', 'yes', 'yes', 'yes'),
        ('medium', 'medium_amount', 'no', 'yes', 'yes'),
    ],
    "auth_random": [
        ('large', '', 'yes', 'yes', 'no'),
        ('medium', 'large_amount', 'yes', 'yes', 'no'),
        ('small', 'large_amount', 'yes', 'yes', 'no'),
        ('large', '', 'no', 'yes', 'no'),
        ('medium', 'large_amount', 'no', 'yes', 'no'),
        ('small', 'large_amount', 'no', 'yes', 'no'),
        ('medium', 'medium_amount', 'yes', 'yes', 'no'),
        ('medium', 'medium_amount', 'no', 'yes', 'no'),
    ],
    "hash_determined": [
        ('large', '', 'no', 'no', 'yes'),
        ('medium', 'large_amount', 'no', 'no', 'yes'),
        ('small', 'large_amount', 'no', 'no', 'yes'),
        ('medium', 'medium_amount', 'yes', 'no', 'yes'),
    ],
    "hash_random": [
        ('large', '', 'no', 'no', 'no'),
        ('medium', 'large_amount', 'no', 'no', 'no'),
        ('small', 'large_amount', 'no', 'no', 'no'),
        ('medium', 'medium_amount', 'yes', 'no', 'no'),
    ],
    "randint_determined": [
        ('medium', 'small_amount', 'yes', 'yes', 'yes'),
        ('medium', 'small_amount', 'no', 'yes', 'yes'),
        ('small', 'medium_amount', 'yes', 'yes', 'yes'),
        ('small', 'medium_amount', 'yes', 'no', 'yes'),
        ('small', 'small_amount', 'yes', 'yes', 'yes'),
        ('small', 'small_amount', 'yes', 'no', 'yes'),
    ],
    "randint_random": [
        ('medium', 'small_amount', 'yes', 'yes', 'no'),
        ('medium', 'small_amount', 'no', 'yes', 'no'),
        ('small', 'medium_amount', 'yes', 'yes', 'no'),
        ('small', 'medium_amount', 'yes', 'no', 'no'),
        ('small', 'small_amount', 'yes', 'yes', 'no'),
        ('small', 'small_amount', 'yes', 'no', 'no'),
    ],
    "counter_determined": [
        ('medium', 'small_amount', 'yes', 'no', 'yes'),
        ('medium', 'small_amount', 'no', 'no', 'yes'),
        ('small', 'medium_amount', 'no', 'yes', 'yes'),
        ('small', 'medium_amount', 'no', 'no', 'yes'),
        ('small', 'small_amount', 'no', 'yes', 'yes'),
        ('small', 'small_amount', 'no', 'no', 'yes'),
    ],
    "counter_random": [
        ('medium', 'small_amount', 'yes', 'no', 'no'),
        ('medium', 'small_amount', 'no', 'no', 'no'),
        ('small', 'medium_amount', 'no', 'yes', 'no'),
        ('small', 'medium_amount', 'no', 'no', 'no'),
        ('small', 'small_amount', 'no', 'yes', 'no'),
        ('small', 'small_amount', 'no', 'no', 'no')
    ]
}

class PseudoFunctionSelectionForm(forms.Form):
    SCENARIO_CHOICES = [
        ('subject_of_pii', "Псевдонімізація виконується суб’єктами персональних даних"),
        ('third_pt_col_pseudo', "Псевдонімізація виконується третьою стороною та передається контролеру"),
        ('cntrl_col_third_pt_pseudo', "Дані збираються з суб’єктів персональних даних контролером даних для подальшої псевдонімізації на стороні процесора"),
        ('cntrl_pseudo_transfer_prcss', "Дані псевдонімізуються контролером даних для подальшої передачі процесору"),
        ('prcss_col_cntrl_pseudo', "Процесор бере участь у зборі даних та передає їх контролеру для подальшої обробки та псевдонімізації"),
        ('cntrl_pseudo', "Дані псевдонімізуються контролером даних для подальшої обробки всередині організації")
    ]
    CHOICES = [
        ('yes', "Так"),
        ('no', "Ні")
    ]
    COMPANY_SIZES = [
        ('small', "Малий обсяг, якщо ваша компанія малого розміру, із менш ніж 50-ма співробітниками, та річним обігом до 10 мільйонів євро"),
        ('medium', "Середній обсяг, якщо ваша компанія середнього розміру, із менш ніж 250-ма співробітниками, та річним обігом до 50-ти мільйонів єврo"),
        ('large', "Великий обсяг, якщо ваша компанія великого розміру, із більше ніж 250-ма співробітниками, та річним обігом більше 50-ти мільйонів євро")
    ]
    CATEGORIES = [
        ('small_amount', "Мала кількість категорій, до 15 категорій персональних даних"),
        ('medium_amount', "Середня кількість категорій, до 40 категорій персональних даних"),
        ('large_amount', "Велика кількість категорій, до 100 категорій персональних даних")        
    ]

    scenario = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect(attrs={'onClick': 'scenarioFunction();'}),
        help_text="Блок сценаріїв обробки даних",
        label="Оберіть сценарій, який найкраще описує підхід до збору та обробки персональних даних у вашій організації",
        choices=SCENARIO_CHOICES
    )
    store_sensitive = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'onClick': 'storeSensitiveFunction();'}),
        help_text="Блок категорії персональних даних. Визначення чутливих даних згідно GDPR https://ec.europa.eu/info/law/law-topic/data-protection/reform/rules-business-and-organisations/legal-grounds-processing-data/sensitive-data/what-personal-data-considered-sensitive_en",
        label="Чи плануєте збирати та обробляти чутливі дані?",
        choices=CHOICES
    )
    company_size = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'onClick': 'companySizeFunction();'}),
        help_text="Обсяг персональних даних визначається на основі розміру компанії за категоріями Європейського парламенту",
        label="Оцініть будь ласка обсяг персональних даних які плануєте обробляти?",
        choices=COMPANY_SIZES
    )
    category = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'onClick': 'categoryFunction();'}),
        help_text="Умовний список таких категорій наведено у Додатку А",
        label="Оцініть будь ласка складність категорій персональних даних, які збиратиме та оброблятиме ваша організація",
        choices=CATEGORIES
    )
    ip_addr = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'onClick': 'ipAddressFunction();'}),
        help_text="Блок перевірки для специфічних типів персональних даних. IP адреса.",
        label="Чи є серед персональних даних, які ви збираєте та обробляєте, IP адреси?",
        choices=CHOICES
    )
    email = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'onClick': 'emailFunction();'}),
        help_text="Блок перевірки для специфічних типів персональних даних. Адреса електронної пошти",
        label="Чи є серед персональних даних які ви збираєте та обробляєте адреса електронної пошти?",
        choices=CHOICES
    )
    use_pseudo = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={'onClick': 'usePseudoFunction();'}),
        help_text="Блок визначення рівня корисності для псевдонімізованих даних",
        label="Чи використовуватимуться псевдонімізовані дані для операційної діяльності вашої організації?",
        choices=CHOICES
    ) 

    def evaluate_form(self):
        cd = self.cleaned_data
        if cd['scenario'] in ['subject_of_pii', 'third_pt_col_pseudo', 'cntrl_col_third_pt_pseudo']:
            pseudo_function = PSEUDO_FUNCTIONS[cd['scenario']]
            return pseudo_function
        elif cd['store_sensitive'] == 'yes':
            pseudo_function = PSEUDO_FUNCTIONS['store_sensitive']
            return pseudo_function
        else:
            searcher = (cd['company_size'], cd['category'], cd['ip_addr'], cd['email'], cd['use_pseudo'])
            result = [k for k in PSEUDO_VAR.keys() if searcher in PSEUDO_VAR[k]]
            pseudo_function = PSEUDO_FUNCTIONS[result[0]]
            return pseudo_function

        