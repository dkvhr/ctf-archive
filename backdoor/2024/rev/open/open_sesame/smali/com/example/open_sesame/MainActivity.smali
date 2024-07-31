.class public Lcom/example/open_sesame/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# static fields
.field private static final valid_password:[I

.field private static final valid_user:Ljava/lang/String; = "Jack Ma"


# instance fields
.field private buttonLogin:Landroid/widget/Button;

.field private editTextPassword:Landroid/widget/EditText;

.field private editTextUsername:Landroid/widget/EditText;


# direct methods
.method static constructor <clinit>()V
    .locals 1

    const/4 v0, 0x7

    new-array v0, v0, [I

    fill-array-data v0, :array_0

    sput-object v0, Lcom/example/open_sesame/MainActivity;->valid_password:[I

    return-void

    nop

    :array_0
    .array-data 4
        0x34
        0x6c
        0x31
        0x62
        0x61
        0x62
        0x61
    .end array-data
.end method

.method public constructor <init>()V
    .locals 0

    .line 11
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method

.method static synthetic access$000(Lcom/example/open_sesame/MainActivity;)V
    .locals 0

    .line 11
    invoke-direct {p0}, Lcom/example/open_sesame/MainActivity;->validateCredentials()V

    return-void
.end method

.method private flag(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    .locals 4

    .line 91
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const/4 v1, 0x0

    .line 92
    :goto_0
    invoke-virtual {p2}, Ljava/lang/String;->length()I

    move-result v2

    if-ge v1, v2, :cond_0

    .line 93
    invoke-virtual {p2, v1}, Ljava/lang/String;->charAt(I)C

    move-result v2

    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v3

    rem-int v3, v1, v3

    invoke-virtual {p1, v3}, Ljava/lang/String;->charAt(I)C

    move-result v3

    xor-int/2addr v2, v3

    int-to-char v2, v2

    .line 94
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    .line 96
    :cond_0
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    return-object p1
.end method

.method private it4chi(Ljava/lang/String;)[I
    .locals 3

    .line 68
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v0

    new-array v0, v0, [I

    const/4 v1, 0x0

    .line 69
    :goto_0
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v2

    if-ge v1, v2, :cond_0

    .line 70
    invoke-virtual {p1, v1}, Ljava/lang/String;->charAt(I)C

    move-result v2

    aput v2, v0, v1

    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_0
    return-object v0
.end method

.method private n4ut1lus(Ljava/lang/String;)Z
    .locals 4

    .line 54
    invoke-direct {p0, p1}, Lcom/example/open_sesame/MainActivity;->it4chi(Ljava/lang/String;)[I

    move-result-object p1

    .line 55
    array-length v0, p1

    sget-object v1, Lcom/example/open_sesame/MainActivity;->valid_password:[I

    array-length v1, v1

    const/4 v2, 0x0

    if-eq v0, v1, :cond_0

    return v2

    :cond_0
    move v0, v2

    .line 59
    :goto_0
    array-length v1, p1

    if-ge v0, v1, :cond_2

    .line 60
    aget v1, p1, v0

    sget-object v3, Lcom/example/open_sesame/MainActivity;->valid_password:[I

    aget v3, v3, v0

    if-eq v1, v3, :cond_1

    return v2

    :cond_1
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_2
    const/4 p1, 0x1

    return p1
.end method

.method private sh4dy(Ljava/lang/String;)Ljava/lang/String;
    .locals 4

    .line 76
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const/4 v1, 0x0

    .line 78
    :goto_0
    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v2

    if-ge v1, v2, :cond_1

    .line 79
    invoke-virtual {p1, v1}, Ljava/lang/String;->charAt(I)C

    move-result v2

    .line 80
    invoke-static {v2}, Ljava/lang/Character;->isDigit(C)Z

    move-result v3

    if-eqz v3, :cond_0

    .line 81
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    :cond_0
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    .line 84
    :cond_1
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    return-object p1
.end method

.method private showToast(Ljava/lang/String;)V
    .locals 1

    const/4 v0, 0x0

    .line 100
    invoke-static {p0, p1, v0}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p1

    invoke-virtual {p1}, Landroid/widget/Toast;->show()V

    return-void
.end method

.method private sl4y3r(Ljava/lang/String;)I
    .locals 0

    .line 87
    invoke-static {p1}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I

    move-result p1

    add-int/lit8 p1, p1, -0x1

    return p1
.end method

.method private validateCredentials()V
    .locals 3

    iget-object v0, p0, Lcom/example/open_sesame/MainActivity;->editTextUsername:Landroid/widget/EditText;

    .line 38
    invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/example/open_sesame/MainActivity;->editTextPassword:Landroid/widget/EditText;

    .line 39
    invoke-virtual {v1}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->trim()Ljava/lang/String;

    move-result-object v1

    const-string v2, "Jack Ma"

    .line 41
    invoke-virtual {v0, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-direct {p0, v1}, Lcom/example/open_sesame/MainActivity;->n4ut1lus(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    .line 42
    invoke-direct {p0, v1}, Lcom/example/open_sesame/MainActivity;->sh4dy(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    .line 43
    invoke-direct {p0, v0}, Lcom/example/open_sesame/MainActivity;->sl4y3r(Ljava/lang/String;)I

    move-result v0

    .line 45
    new-instance v1, Ljava/lang/StringBuilder;

    const-string v2, "flag{"

    invoke-direct {v1, v2}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-static {v0}, Ljava/lang/Integer;->toString(I)Ljava/lang/String;

    move-result-object v0

    const-string v2, "U|]rURuoU^PoR_FDMo@X]uBUg"

    invoke-direct {p0, v0, v2}, Lcom/example/open_sesame/MainActivity;->flag(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "}"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    goto :goto_0

    :cond_0
    const-string v0, "Invalid credentials. Please try again."

    .line 49
    invoke-direct {p0, v0}, Lcom/example/open_sesame/MainActivity;->showToast(Ljava/lang/String;)V

    :goto_0
    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1

    .line 22
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 23
    sget p1, Lcom/example/open_sesame/R$layout;->activity_main:I

    invoke-virtual {p0, p1}, Lcom/example/open_sesame/MainActivity;->setContentView(I)V

    .line 25
    sget p1, Lcom/example/open_sesame/R$id;->editTextUsername:I

    invoke-virtual {p0, p1}, Lcom/example/open_sesame/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/EditText;

    iput-object p1, p0, Lcom/example/open_sesame/MainActivity;->editTextUsername:Landroid/widget/EditText;

    .line 26
    sget p1, Lcom/example/open_sesame/R$id;->editTextPassword:I

    invoke-virtual {p0, p1}, Lcom/example/open_sesame/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/EditText;

    iput-object p1, p0, Lcom/example/open_sesame/MainActivity;->editTextPassword:Landroid/widget/EditText;

    .line 27
    sget p1, Lcom/example/open_sesame/R$id;->buttonLogin:I

    invoke-virtual {p0, p1}, Lcom/example/open_sesame/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/Button;

    iput-object p1, p0, Lcom/example/open_sesame/MainActivity;->buttonLogin:Landroid/widget/Button;

    .line 29
    new-instance v0, Lcom/example/open_sesame/MainActivity$1;

    invoke-direct {v0, p0}, Lcom/example/open_sesame/MainActivity$1;-><init>(Lcom/example/open_sesame/MainActivity;)V

    invoke-virtual {p1, v0}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
.end method
