package androidx.compose.foundation.text;

import androidx.compose.ui.input.key.Key;
import androidx.compose.ui.input.key.KeyEvent;
import androidx.compose.ui.input.key.KeyEvent_androidKt;
import kotlin.Metadata;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.Intrinsics;
import kotlin.jvm.internal.PropertyReference1Impl;

/* compiled from: KeyMapping.kt */
@Metadata(d1 = {"\u0000\u0018\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u000b\n\u0000\u001a\u001f\u0010\u0004\u001a\u00020\u00012\u0012\u0010\u0005\u001a\u000e\u0012\u0004\u0012\u00020\u0007\u0012\u0004\u0012\u00020\b0\u0006H\u0000ø\u0001\u0000\"\u0014\u0010\u0000\u001a\u00020\u0001X\u0080\u0004¢\u0006\b\n\u0000\u001a\u0004\b\u0002\u0010\u0003\u0082\u0002\u0004\n\u0002\b\u0019¨\u0006\t"}, d2 = {"defaultKeyMapping", "Landroidx/compose/foundation/text/KeyMapping;", "getDefaultKeyMapping", "()Landroidx/compose/foundation/text/KeyMapping;", "commonKeyMapping", "shortcutModifier", "Lkotlin/Function1;", "Landroidx/compose/ui/input/key/KeyEvent;", "", "foundation_release"}, k = 2, mv = {1, 8, 0}, xi = 48)
/* loaded from: classes.dex */
public final class KeyMappingKt {
    private static final KeyMapping defaultKeyMapping;

    public static final KeyMapping getDefaultKeyMapping() {
        return defaultKeyMapping;
    }

    public static final KeyMapping commonKeyMapping(final Function1<? super KeyEvent, Boolean> shortcutModifier) {
        Intrinsics.checkNotNullParameter(shortcutModifier, "shortcutModifier");
        return new KeyMapping() { // from class: androidx.compose.foundation.text.KeyMappingKt$commonKeyMapping$1
            @Override // androidx.compose.foundation.text.KeyMapping
            /* renamed from: map-ZmokQxo */
            public KeyCommand mo759mapZmokQxo(android.view.KeyEvent event) {
                Intrinsics.checkNotNullParameter(event, "event");
                if (shortcutModifier.invoke(KeyEvent.m3598boximpl(event)).booleanValue() && KeyEvent_androidKt.m3621isShiftPressedZmokQxo(event)) {
                    if (Key.m3307equalsimpl0(KeyEvent_androidKt.m3615getKeyZmokQxo(event), MappedKeys.INSTANCE.m794getZEK5gGoQ())) {
                        return KeyCommand.REDO;
                    }
                    return null;
                }
                if (shortcutModifier.invoke(KeyEvent.m3598boximpl(event)).booleanValue()) {
                    long m3615getKeyZmokQxo = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m774getCEK5gGoQ()) || Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m784getInsertEK5gGoQ())) {
                        return KeyCommand.COPY;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m791getVEK5gGoQ())) {
                        return KeyCommand.PASTE;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m792getXEK5gGoQ())) {
                        return KeyCommand.CUT;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m771getAEK5gGoQ())) {
                        return KeyCommand.SELECT_ALL;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m793getYEK5gGoQ())) {
                        return KeyCommand.REDO;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m794getZEK5gGoQ())) {
                        return KeyCommand.UNDO;
                    }
                    return null;
                }
                if (KeyEvent_androidKt.m3619isCtrlPressedZmokQxo(event)) {
                    return null;
                }
                if (KeyEvent_androidKt.m3621isShiftPressedZmokQxo(event)) {
                    long m3615getKeyZmokQxo2 = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m779getDirectionLeftEK5gGoQ())) {
                        return KeyCommand.SELECT_LEFT_CHAR;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m780getDirectionRightEK5gGoQ())) {
                        return KeyCommand.SELECT_RIGHT_CHAR;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m781getDirectionUpEK5gGoQ())) {
                        return KeyCommand.SELECT_UP;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m778getDirectionDownEK5gGoQ())) {
                        return KeyCommand.SELECT_DOWN;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m788getPageUpEK5gGoQ())) {
                        return KeyCommand.SELECT_PAGE_UP;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m787getPageDownEK5gGoQ())) {
                        return KeyCommand.SELECT_PAGE_DOWN;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m786getMoveHomeEK5gGoQ())) {
                        return KeyCommand.SELECT_LINE_START;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m785getMoveEndEK5gGoQ())) {
                        return KeyCommand.SELECT_LINE_END;
                    }
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m784getInsertEK5gGoQ())) {
                        return KeyCommand.PASTE;
                    }
                    return null;
                }
                long m3615getKeyZmokQxo3 = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m779getDirectionLeftEK5gGoQ())) {
                    return KeyCommand.LEFT_CHAR;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m780getDirectionRightEK5gGoQ())) {
                    return KeyCommand.RIGHT_CHAR;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m781getDirectionUpEK5gGoQ())) {
                    return KeyCommand.UP;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m778getDirectionDownEK5gGoQ())) {
                    return KeyCommand.DOWN;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m788getPageUpEK5gGoQ())) {
                    return KeyCommand.PAGE_UP;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m787getPageDownEK5gGoQ())) {
                    return KeyCommand.PAGE_DOWN;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m786getMoveHomeEK5gGoQ())) {
                    return KeyCommand.LINE_START;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m785getMoveEndEK5gGoQ())) {
                    return KeyCommand.LINE_END;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m782getEnterEK5gGoQ())) {
                    return KeyCommand.NEW_LINE;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m773getBackspaceEK5gGoQ())) {
                    return KeyCommand.DELETE_PREV_CHAR;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m777getDeleteEK5gGoQ())) {
                    return KeyCommand.DELETE_NEXT_CHAR;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m789getPasteEK5gGoQ())) {
                    return KeyCommand.PASTE;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m776getCutEK5gGoQ())) {
                    return KeyCommand.CUT;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m775getCopyEK5gGoQ())) {
                    return KeyCommand.COPY;
                }
                if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m790getTabEK5gGoQ())) {
                    return KeyCommand.TAB;
                }
                return null;
            }
        };
    }

    static {
        final KeyMapping commonKeyMapping = commonKeyMapping(new PropertyReference1Impl() { // from class: androidx.compose.foundation.text.KeyMappingKt$defaultKeyMapping$1
            @Override // kotlin.jvm.internal.PropertyReference1Impl, kotlin.reflect.KProperty1
            public Object get(Object obj) {
                return Boolean.valueOf(KeyEvent_androidKt.m3619isCtrlPressedZmokQxo(((KeyEvent) obj).m3604unboximpl()));
            }
        });
        defaultKeyMapping = new KeyMapping() { // from class: androidx.compose.foundation.text.KeyMappingKt$defaultKeyMapping$2$1
            @Override // androidx.compose.foundation.text.KeyMapping
            /* renamed from: map-ZmokQxo */
            public KeyCommand mo759mapZmokQxo(android.view.KeyEvent event) {
                Intrinsics.checkNotNullParameter(event, "event");
                KeyCommand keyCommand = null;
                if (KeyEvent_androidKt.m3621isShiftPressedZmokQxo(event) && KeyEvent_androidKt.m3619isCtrlPressedZmokQxo(event)) {
                    long m3615getKeyZmokQxo = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m779getDirectionLeftEK5gGoQ())) {
                        keyCommand = KeyCommand.SELECT_LEFT_WORD;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m780getDirectionRightEK5gGoQ())) {
                        keyCommand = KeyCommand.SELECT_RIGHT_WORD;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m781getDirectionUpEK5gGoQ())) {
                        keyCommand = KeyCommand.SELECT_PREV_PARAGRAPH;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo, MappedKeys.INSTANCE.m778getDirectionDownEK5gGoQ())) {
                        keyCommand = KeyCommand.SELECT_NEXT_PARAGRAPH;
                    }
                } else if (KeyEvent_androidKt.m3619isCtrlPressedZmokQxo(event)) {
                    long m3615getKeyZmokQxo2 = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m779getDirectionLeftEK5gGoQ())) {
                        keyCommand = KeyCommand.LEFT_WORD;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m780getDirectionRightEK5gGoQ())) {
                        keyCommand = KeyCommand.RIGHT_WORD;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m781getDirectionUpEK5gGoQ())) {
                        keyCommand = KeyCommand.PREV_PARAGRAPH;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m778getDirectionDownEK5gGoQ())) {
                        keyCommand = KeyCommand.NEXT_PARAGRAPH;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m783getHEK5gGoQ())) {
                        keyCommand = KeyCommand.DELETE_PREV_CHAR;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m777getDeleteEK5gGoQ())) {
                        keyCommand = KeyCommand.DELETE_NEXT_WORD;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m773getBackspaceEK5gGoQ())) {
                        keyCommand = KeyCommand.DELETE_PREV_WORD;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo2, MappedKeys.INSTANCE.m772getBackslashEK5gGoQ())) {
                        keyCommand = KeyCommand.DESELECT;
                    }
                } else if (KeyEvent_androidKt.m3621isShiftPressedZmokQxo(event)) {
                    long m3615getKeyZmokQxo3 = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m786getMoveHomeEK5gGoQ())) {
                        keyCommand = KeyCommand.SELECT_LINE_LEFT;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo3, MappedKeys.INSTANCE.m785getMoveEndEK5gGoQ())) {
                        keyCommand = KeyCommand.SELECT_LINE_RIGHT;
                    }
                } else if (KeyEvent_androidKt.m3618isAltPressedZmokQxo(event)) {
                    long m3615getKeyZmokQxo4 = KeyEvent_androidKt.m3615getKeyZmokQxo(event);
                    if (Key.m3307equalsimpl0(m3615getKeyZmokQxo4, MappedKeys.INSTANCE.m773getBackspaceEK5gGoQ())) {
                        keyCommand = KeyCommand.DELETE_FROM_LINE_START;
                    } else if (Key.m3307equalsimpl0(m3615getKeyZmokQxo4, MappedKeys.INSTANCE.m777getDeleteEK5gGoQ())) {
                        keyCommand = KeyCommand.DELETE_TO_LINE_END;
                    }
                }
                return keyCommand == null ? KeyMapping.this.mo759mapZmokQxo(event) : keyCommand;
            }
        };
    }
}
