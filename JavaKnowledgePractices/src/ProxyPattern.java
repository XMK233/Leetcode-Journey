import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

interface UserDao{
    void save();
}

interface UserJian{
    void use();
}

class UserDaoImpl implements UserDao{
    public void save(){
        System.out.println("苗刀, 撩刀");
    }
}

class UserJianImpl implements UserJian {
    public void use(){
        System.out.println("剑, 云剑");
    }
}

class InvocationHandlerImpl implements InvocationHandler{
    private Object target;
    public InvocationHandlerImpl(Object obj){
        this.target = obj;
    }
    public Object invoke (Object proxy, Method method, Object[] args) throws Throwable{
        System.out.println("磨");
        Object result = method.invoke(target, args);
        System.out.println("擦");
        return result;
    }
}

public class ProxyPattern {

    public static void main(String[] args) {
//        UserDao udi = new UserDaoImpl();
        UserJian uj = new UserJianImpl(); //UserJianImpl();
        InvocationHandlerImpl ihi = new InvocationHandlerImpl(uj);

        ClassLoader loader = uj.getClass().getClassLoader();
        Class<?>[] interfaces = uj.getClass().getInterfaces();

        UserJian newProxyInstance = (UserJian) Proxy.newProxyInstance(loader, interfaces, ihi);
        newProxyInstance.use();
    }
}
