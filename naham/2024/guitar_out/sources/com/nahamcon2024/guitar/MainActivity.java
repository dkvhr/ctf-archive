package com.nahamcon2024.guitar;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import androidx.activity.ComponentActivity;
import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;

/* compiled from: MainActivity.kt */
@Metadata(d1 = {"\u0000&\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0000\b\u0007\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\u0012\u0010\u0005\u001a\u00020\u00062\b\u0010\u0007\u001a\u0004\u0018\u00010\bH\u0014J\b\u0010\t\u001a\u00020\u0006H\u0014J\u0010\u0010\n\u001a\u00020\u00062\u0006\u0010\u000b\u001a\u00020\fH\u0002R\u000e\u0010\u0003\u001a\u00020\u0004X\u0082.¢\u0006\u0002\n\u0000¨\u0006\r"}, d2 = {"Lcom/nahamcon2024/guitar/MainActivity;", "Landroidx/activity/ComponentActivity;", "()V", "mediaPlayer", "Landroid/media/MediaPlayer;", "onCreate", "", "savedInstanceState", "Landroid/os/Bundle;", "onDestroy", "playSound", "resId", "", "app_release"}, k = 1, mv = {1, 9, 0}, xi = 48)
/* loaded from: classes.dex */
public final class MainActivity extends ComponentActivity {
    public static final int $stable = 8;
    private MediaPlayer mediaPlayer;

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        View findViewById = findViewById(R.id.btnNote1);
        Intrinsics.checkNotNullExpressionValue(findViewById, "findViewById(...)");
        View findViewById2 = findViewById(R.id.btnNote2);
        Intrinsics.checkNotNullExpressionValue(findViewById2, "findViewById(...)");
        View findViewById3 = findViewById(R.id.btnNote3);
        Intrinsics.checkNotNullExpressionValue(findViewById3, "findViewById(...)");
        View findViewById4 = findViewById(R.id.btnNote4);
        Intrinsics.checkNotNullExpressionValue(findViewById4, "findViewById(...)");
        View findViewById5 = findViewById(R.id.btnNote5);
        Intrinsics.checkNotNullExpressionValue(findViewById5, "findViewById(...)");
        View findViewById6 = findViewById(R.id.btnNote6);
        Intrinsics.checkNotNullExpressionValue(findViewById6, "findViewById(...)");
        ((Button) findViewById).setOnClickListener(new View.OnClickListener() { // from class: com.nahamcon2024.guitar.MainActivity$$ExternalSyntheticLambda0
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.onCreate$lambda$0(MainActivity.this, view);
            }
        });
        ((Button) findViewById2).setOnClickListener(new View.OnClickListener() { // from class: com.nahamcon2024.guitar.MainActivity$$ExternalSyntheticLambda1
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.onCreate$lambda$1(MainActivity.this, view);
            }
        });
        ((Button) findViewById3).setOnClickListener(new View.OnClickListener() { // from class: com.nahamcon2024.guitar.MainActivity$$ExternalSyntheticLambda2
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.onCreate$lambda$2(MainActivity.this, view);
            }
        });
        ((Button) findViewById4).setOnClickListener(new View.OnClickListener() { // from class: com.nahamcon2024.guitar.MainActivity$$ExternalSyntheticLambda3
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.onCreate$lambda$3(MainActivity.this, view);
            }
        });
        ((Button) findViewById5).setOnClickListener(new View.OnClickListener() { // from class: com.nahamcon2024.guitar.MainActivity$$ExternalSyntheticLambda4
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.onCreate$lambda$4(MainActivity.this, view);
            }
        });
        ((Button) findViewById6).setOnClickListener(new View.OnClickListener() { // from class: com.nahamcon2024.guitar.MainActivity$$ExternalSyntheticLambda5
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.onCreate$lambda$5(MainActivity.this, view);
            }
        });
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final void onCreate$lambda$0(MainActivity this$0, View view) {
        Intrinsics.checkNotNullParameter(this$0, "this$0");
        this$0.playSound(R.raw.e);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final void onCreate$lambda$1(MainActivity this$0, View view) {
        Intrinsics.checkNotNullParameter(this$0, "this$0");
        this$0.playSound(R.raw.a);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final void onCreate$lambda$2(MainActivity this$0, View view) {
        Intrinsics.checkNotNullParameter(this$0, "this$0");
        this$0.playSound(R.raw.d);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final void onCreate$lambda$3(MainActivity this$0, View view) {
        Intrinsics.checkNotNullParameter(this$0, "this$0");
        this$0.playSound(R.raw.g);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final void onCreate$lambda$4(MainActivity this$0, View view) {
        Intrinsics.checkNotNullParameter(this$0, "this$0");
        this$0.playSound(R.raw.b);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final void onCreate$lambda$5(MainActivity this$0, View view) {
        Intrinsics.checkNotNullParameter(this$0, "this$0");
        this$0.playSound(R.raw.e2);
    }

    private final void playSound(int resId) {
        MediaPlayer mediaPlayer = this.mediaPlayer;
        MediaPlayer mediaPlayer2 = null;
        if (mediaPlayer != null) {
            if (mediaPlayer == null) {
                Intrinsics.throwUninitializedPropertyAccessException("mediaPlayer");
                mediaPlayer = null;
            }
            mediaPlayer.release();
        }
        MediaPlayer create = MediaPlayer.create(this, resId);
        Intrinsics.checkNotNullExpressionValue(create, "create(...)");
        this.mediaPlayer = create;
        if (create == null) {
            Intrinsics.throwUninitializedPropertyAccessException("mediaPlayer");
        } else {
            mediaPlayer2 = create;
        }
        mediaPlayer2.start();
    }

    @Override // android.app.Activity
    protected void onDestroy() {
        super.onDestroy();
        MediaPlayer mediaPlayer = this.mediaPlayer;
        if (mediaPlayer != null) {
            if (mediaPlayer == null) {
                Intrinsics.throwUninitializedPropertyAccessException("mediaPlayer");
                mediaPlayer = null;
            }
            mediaPlayer.release();
        }
    }
}
